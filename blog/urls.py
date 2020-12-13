from django.urls import path
from .views import (
      PostListView, 
      PostDetailView, 
      PostCreateView, 
      PostUpdateView, 
      PostDeleteView,
      UserPostListView
      )
from . import views

urlpatterns = [
      path('', PostListView.as_view(), name='blog-home'),
      path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
      path('about/', views.about, name='blog-about'),#we got navigated here from our urls.py of 
      #project and here it will look for the path after first forward slash ex"www.blog/about/" 
      # here it will chopped off the 'blog/' part and now looking for rest of the path 
      #from here we will navigate to 'view' page and look for 'about' function
      path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
      path('post/new/', PostCreateView.as_view(), name='post-create'),
      path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
      path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]