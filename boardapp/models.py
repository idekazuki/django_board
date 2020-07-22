from django.db import models
from django.utils import timezone


# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=200, null=True, blank=True, default='a')
    update_at = models.DateTimeField(auto_now=True)

class Tweet(models.Model):
    uni_id = models.IntegerField()
    text = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    user_name = models.CharField(max_length=50)
    user_screen_name = models.CharField(max_length=50)
    
class Qiita(models.Model):
    followers_count = models.IntegerField()
    icon_url = models.CharField(max_length=100)
    items = models.CharField(max_length=20)
    items_count = models.IntegerField()
    