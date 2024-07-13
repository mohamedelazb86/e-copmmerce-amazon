from django.shortcuts import render
from products.models import Product,Brand,Review
from django.db.models.aggregates import Count

def index(request):
    brands=Brand.objects.all().annotate(product_count=Count('product_brand'))[:10]
    sale_product=Product.objects.all()[:10]
    reviews=Review.objects.all()[:10]

    context={
        'brands':brands,
        'sale_product':sale_product,
        'reviews':reviews
    }
    return render(request,'settings/index.html',context)
