from django.urls import path
from .views import post_detatil,post_list,create_post,update_post,delete_post


urlpatterns = [
    path('',post_list),
    path('<slug:slug>',post_detatil),
    path('<slug:slug>/create',create_post),
    path('<slug:slug>/update',update_post),
    path('<slug:slug>/delete',delete_post),
]
