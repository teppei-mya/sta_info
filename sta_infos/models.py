from django.db import models
from django.contrib.auth.models import User

class Stadium(models.Model):
    """スタジアムを表す"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    audience = models.CharField(max_length=50)
    club = models.CharField(max_length=200)

    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.name

class Topic(models.Model):
    """トピックを表す"""
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, default=0)
    text = models.CharField(max_length=50)

    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.text

class Shop(models.Model):
    """お店を表す"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    distance = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.name

class Review(models.Model):
    """レビューを表す"""
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=0)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.text