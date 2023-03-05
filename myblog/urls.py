from django.urls import path, include
from django.urls.resolvers import URLPattern 
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,userListView
urlpatterns = [
    #path('',views.home,name='home-page'),
    path('',PostListView.as_view(),name='home-page'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('user/<str:username>/',userListView.as_view(),name='user-posts'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name='about-page'),
    
]
