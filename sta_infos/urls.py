"""sta_infosのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'sta_infos'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # 全体地図を表示
    path('mainmap/', views.mainmap, name='mainmap'),
    # 個別スタジアムページ
    path('stadium/<int:stadium_id>', views.stadium, name='stadium'),
    # トピックごとのレビュー一覧表示
    path('stadium/<int:stadium_id>/<int:topic_id>', views.topic, name='topic'),
    # お店の口コミ
    path('stadium/<int:stadium_id>/<int:topic_id>/<int:shop_id>', views.shop, name='shop'),
    # 新規店舗の追加ページ
    path('stadium/<int:stadium_id>/<int:topic_id>/new_shop/', views.new_shop, name='new_shop'),
    # 店舗の編集ページ
    path('stadium/<int:stadium_id>/<int:topic_id>/<int:shop_id>/edit_shop/', views.edit_shop, name='edit_shop'),
    # 新規口コミの追加ページ
    path('stadium/<int:stadium_id>/<int:topic_id>/<int:shop_id>/new_review/', views.new_review, name='new_review'),
    # 口コミの編集ページ
    path('stadium/<int:stadium_id>/<int:topic_id>/<int:shop_id>/<int:review_id>/edit_review/', views.edit_review, name='edit_review'),
    # 口コミの削除ページ
    path('stadium/<int:stadium_id>/<int:topic_id>/<int:shop_id>/<int:review_id>/delete_review/', views.delete_review, name='delete_review'),
]