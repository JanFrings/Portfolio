from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, TemplateView,
                                CreateView, DeleteView
                                DetailView, UpdateView)
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PostListView(ListView):
    model = Post
    # find out how to specify which model fields should be displayed in the listview
    def get_query_set(self):
        return Post.object.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostDraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    model = Post

    def get_query_set(self):
        return Post.object.filter(published_date__isnull=True).order_by('created_date')
