from django.contrib import admin
from .models import BoardModel, Qiita, Tweet
# Register your models here.
admin.site.register(BoardModel)
admin.site.register(Qiita)
admin.site.register(Tweet)