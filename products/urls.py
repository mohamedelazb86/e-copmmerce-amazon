from django.urls import path
from .views import Product_List,Product_detail,Brand_Detail,Brand_List,add_review
from .api import ProductApi,ProductDetailApi

urlpatterns = [

    path('brands',Brand_List.as_view()),
    path('<slug:slug>/brands',Brand_Detail.as_view()),

    path('',Product_List.as_view()),
    path('<slug:slug>',Product_detail.as_view()),
    path('<slug:slug>/add_review',add_review),
    
    # api url
    path('api/productlist',ProductApi.as_view()),
    path('api/productDetail/<int:pk>',ProductDetailApi.as_view()),
]
