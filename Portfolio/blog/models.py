from django.db import models
from django.conf import settings

from django.contrib import auth

from django.utils import timezone
from django.urls import reverse

from django.conf import settings

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return '@{}'.format(self.username)



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    mentor = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', blank=True)
    url = models.URLField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absoulte_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
