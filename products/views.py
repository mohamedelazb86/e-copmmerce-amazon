from django.shortcuts import render,redirect
from .models import Product,Brand,Review,ProductImge
from django.views.generic import ListView,DetailView

class Product_List(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=28
    
class Product_detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["images"] = ProductImge.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)

        return context
    



class Brand_List(ListView):
    model=Brand
    template_name='products/brand_list.html'
    

class Brand_Detail(DetailView):
    model=Brand
    template_name='products/brand_detail.html'


def add_review(request,slug):
    user=request.user
    product=Product.objects.get(slug=slug)
    rate=request.POST['rating']
    review=request.POST['rate']
    Review.objects.create(
        user=user,
        product=product,
        rate=rate,
        content=review
    )
    return redirect(f'/products/{slug}')

