from django.urls import path
from .views import post_detatil,post_list,create_post,update_post,delete_post
from .api import PostLiSTaPI,PostDetailApi,Post_update_Createapi

urlpatterns = [
    path('',post_list),
    path('<slug:slug>',post_detatil),
    path('<slug:slug>/create',create_post),
    path('<slug:slug>/update',update_post),
    path('<slug:slug>/delete',delete_post),

    # url api
    path('api/post_list',PostLiSTaPI.as_view()),
    path('api/post_detail/<int:pk>',PostDetailApi.as_view()),
    path('api/create/TEST/TEST/<int:pk>',Post_update_Createapi.as_view()),
]

