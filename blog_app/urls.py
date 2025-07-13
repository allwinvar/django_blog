from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog, name='blog'),
    path('blog/admin_signin',views.admin_login,name='blog/admin_signin'),
    path('blog/admin',views.blog_admin, name='blog/admin'),
    path('blog/post',views.post,name='blog/post'),
    path('blog/admin/create_post',views.create_post, name='blog/admin/create_post'),
    path('blog/category/<slug:category_slug>/', views.post_list_by_category, name='post_list_by_category_paginated'),
    path('blog/category/<slug:category_slug>/<int:post_id>/', views.post_detail, name='post_details'),
]
