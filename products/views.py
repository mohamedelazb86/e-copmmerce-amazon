from django.shortcuts import render
from .models import Product,Brand
from django.views.generic import ListView,DetailView

class Product_List(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=28
    
class Product_detail(DetailView):
    model=Product
    template_name='products/product_detail.html'



class Brand_List(ListView):
    model=Brand
    template_name='products/brand_list.html'
    

class Brand_Detail(DetailView):
    model=Brand
    template_name='products/brand_detail.html'
