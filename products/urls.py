from django.urls import path
from .views import Product_List,Product_detail,Brand_Detail,Brand_List


urlpatterns = [

    path('brands',Brand_List.as_view()),
    path('<slug:slug>/brands',Brand_Detail.as_view()),

    path('',Product_List.as_view()),
    path('<slug:slug>',Product_detail.as_view()),
]
