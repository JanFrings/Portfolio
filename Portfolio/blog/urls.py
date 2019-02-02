from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/list/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/draft/', views.PostDraftListView.as_view(), name='post_draft'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='post_comment'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('login/', auth_view.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
