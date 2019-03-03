from django.conf.urls import url
from django.urls import path
from . import views

app_name='dashboard'

urlpatterns=[
path('',views.PostListView.as_view(),name='all'),
path('new/',views.CreatePost.as_view(),name='create'),
path('by/<username>/',views.StartupPosts.as_view(),name='startup'),
path('by/<username>/<int:pk>/',views.PostDetail.as_view(),name='single'),
path('delete/<int:pk>',views.DeletePost.as_view(),name='delete')



]
