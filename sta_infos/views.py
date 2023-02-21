from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core import serializers
import json
from .models import Stadium, Topic, Shop, Review
from .forms import ShopForm, ReviewForm

def index(request):
    """sta_infoのホームページ"""
    return render(request, 'sta_infos/index.html')

def mainmap(request):
    """全体地図を表示"""
    stadiums = Stadium.objects.all()
    list = []
    for stadium in stadiums:
        list.append(stadium)
    stadium_list = serializers.serialize("json", list)
    context = {'stadiums': stadium_list}
    return render(request, 'sta_infos/mainmap.html', context)

def stadium(request, stadium_id):
    """個別スタジアムページの表示"""
    stadium = Stadium.objects.get(id=stadium_id)
    list = [stadium]
    stadium_list = serializers.serialize("json", list)
    topics = stadium.topic_set.all()
    context = {'stadium':stadium, 'topics':topics, 'stadium_list':stadium_list}
    return render(request, 'sta_infos/stadium.html', context)

def topic(request, stadium_id, topic_id):
    """トピックごとのレビュー表示"""
    stadium = Stadium.objects.get(id=stadium_id)
    list1 = [stadium]
    stadium_list = serializers.serialize("json", list1)
    topic = stadium.topic_set.get(id=topic_id)
    list2 = [topic]
    topic_list = serializers.serialize("json", list2)
    shops = topic.shop_set.order_by('distance')
    list3 = []
    for shop in shops:
        list3.append(shop)
    shop_list = serializers.serialize("json", list3)
    context = {'stadium':stadium, 'topic':topic, 'shops':shops, 'stadium_list':stadium_list, 'topic_list': topic_list,'shop_list':shop_list}
    return render(request, 'sta_infos/topic.html', context)

def shop(request, stadium_id, topic_id, shop_id):
    """お店の表示"""
    stadium = Stadium.objects.get(id=stadium_id)
    topic = stadium.topic_set.get(id=topic_id)
    shop = topic.shop_set.get(id=shop_id)
    list = [shop]
    shop_list = serializers.serialize("json", list)
    reviews = shop.review_set.order_by('-date_added')
    context = {'stadium':stadium, 'topic':topic, 'shop':shop, 'reviews': reviews, 'shop_list':shop_list}
    return render(request, 'sta_infos/shop.html', context)

@login_required
def new_shop(request, stadium_id, topic_id):
    """新規店舗を追加する"""
    stadium = Stadium.objects.get(id=stadium_id)
    list = [stadium]
    stadium_list = serializers.serialize("json", list)
    topic = stadium.topic_set.get(id=topic_id)
    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = ShopForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = ShopForm(data=request.POST)
        if form.is_valid():
            new_shop = form.save(commit=False)
            new_shop.topic = topic
            new_shop.save()
            return redirect('sta_infos:topic', stadium_id=stadium_id, topic_id=topic_id)
    
    # 空または無効のフォームを表示する
    context = {'form':form, 'stadium':stadium, 'topic':topic, 'stadium_list':stadium_list}
    return render(request, 'sta_infos/new_shop.html', context)

@login_required
def edit_shop(request, stadium_id, topic_id, shop_id):
    """既存の店舗を編集する"""
    shop = Shop.objects.get(id=shop_id)
    list = [shop]
    shop_list = serializers.serialize("json", list)
    topic = shop.topic
    stadium = topic.stadium

    if request.method != 'POST':
        # 初回リクエスト時は現在の店舗の内容がフォームに埋め込まれる
        form = ShopForm(instance=shop)
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = ShopForm(instance=shop, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('sta_infos:shop', stadium_id=stadium.id, topic_id=topic.id, shop_id=shop.id)
    
    context = {'form':form, 'stadium':stadium, 'topic':topic, 'shop':shop, 'shop_list':shop_list}
    return render(request, 'sta_infos/edit_shop.html', context)

@login_required
def new_review(request, stadium_id, topic_id, shop_id):
    """新規口コミを追加する"""
    shop = Shop.objects.get(id=shop_id)
    topic = shop.topic
    stadium = topic.stadium

    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = ReviewForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.shop = shop
            new_review.owner = request.user
            new_review.save()
            return redirect('sta_infos:shop', stadium_id=stadium_id, topic_id=topic_id, shop_id=shop_id)
    
    # 空または無効のフォームを表示する
    context = {'form':form, 'stadium':stadium, 'topic':topic, 'shop':shop}
    return render(request, 'sta_infos/new_review.html', context)

@login_required
def edit_review(request, stadium_id, topic_id, shop_id, review_id):
    """既存の口コミを編集する"""
    review = Review.objects.get(id=review_id)
    if review.owner != request.user:
        raise Http404
    
    shop = review.shop
    topic = shop.topic
    stadium = topic.stadium

    if request.method != 'POST':
        # 初回リクエスト時は現在の口コミの内容がフォームに埋め込まれている
        form =  ReviewForm(instance=review)
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('sta_infos:shop', stadium_id=stadium.id, topic_id=topic.id, shop_id=shop.id)
    
    context = {'form':form, 'stadium':stadium, 'topic':topic, 'shop':shop, 'review':review}
    return render(request, 'sta_infos/edit_review.html', context)

@login_required
def delete_review(request, stadium_id, topic_id, shop_id, review_id):
    """既存の口コミを削除する"""
    review = Review.objects.get(id=review_id)
    if review.owner != request.user:
        raise Http404
    
    shop = review.shop
    topic = shop.topic
    stadium = topic.stadium

    if request.method == 'POST':
        review.delete()
        return redirect('sta_infos:shop', stadium_id=stadium.id, topic_id=topic.id, shop_id=shop.id)
    
    context = {'stadium':stadium, 'topic':topic, 'shop':shop, 'review':review}
    return render(request, 'sta_infos/delete_review.html', context)