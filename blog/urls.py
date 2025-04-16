from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
]
