from django.contrib import admin
from .models import UserModel, Post, Comment
# Register your models here.
admin.site.register(UserModel)
admin.site.register(Post)
admin.site.register(Comment)
