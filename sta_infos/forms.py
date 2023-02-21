from django import forms

from .models import Shop, Review

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'lat', 'lon', 'distance']
        labels = {'name':'店舗名', 'address':'住所', 'lat':'緯度', 'lon':'経度', 'distance': 'スタジアムまでの距離（m）'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text':''}