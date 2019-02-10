from django.views.generic import (ListView, TemplateView,
                                CreateView, DeleteView,
                                DetailView, UpdateView)

from blog.models import Post, Comment, User
from django import forms
from .forms import PostForm, CommentForm, UserForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()

# ////////////////////////////LoginViews////////////////////////////

class SignUpView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# ////////////////////////////PostViews////////////////////////////

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        # -published_date -> the (-)minus orders the list in a way that the most rescent one is first


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):

    #LoginRequiredMixin attributes
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    #CreateView attributes
    form_class = PostForm
    model = Post

    # passing the current user object to post.author within the validation
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    # so for there is no user interface to get to the deleteview but only a superuser should be allowed to delete

    #LoginRequiredMixin attributes
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    #DeleteView attributes
    model = Post
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']



def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post             #assigns the post object call in the beginning to the comment.post model field
            comment.author = request.user   #assigns the current user to the author field in the model
            comment.save()
        return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
        dic_form = {'form':form}
        return render(request, 'blog/comment_form.html', dic_form)
