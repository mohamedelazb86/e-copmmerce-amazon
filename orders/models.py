from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.utils import timezone
from products.models import Product
from accounts.models import Address


STATUS_ORDER=[
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
    ]
class Order(models.Model):
    user=models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=120,choices=STATUS_ORDER)
    code=models.CharField(max_length=120,default=generate_code)
    order_time=models.DateTimeField(default=timezone.now)
    delivery_time=models.DateTimeField(null=True,blank=True)
    delivery_address=models.ForeignKey(Address,related_name='order_address',on_delete=models.SET_NULL,null=True,blank=True)
    copoun=models.ForeignKey('Copoun',related_name='order_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    total=models.FloatField(null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='detail_order')
    product=models.ForeignKey(Product,related_name='detail_product',on_delete=models.CASCADE)
    quantity=models.FloatField()
    price=models.FloatField()
    total=models.FloatField(null=True,blank=True)

STATUS_CART=[
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
    
    ]
class Cart(models.Model):
    user=models.ForeignKey(User,related_name='cart_user',on_delete=models.CASCADE)
    status=models.CharField(max_length=120,choices=STATUS_CART)
    
    copoun=models.ForeignKey('Copoun',related_name='cart_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    
    total_with_copoun=models.FloatField(null=True,blank=True)


class CartDetail(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='detail_cart')
    product=models.ForeignKey(Product,related_name='detailcart_product',on_delete=models.CASCADE)
    quantity=models.FloatField(default=1)
    
    total=models.FloatField(null=True,blank=True)

class Copoun(models.Model):
    code=models.CharField(max_length=120)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(null=True,blank=True)
    quantity=models.FloatField()
    
    discount=models.FloatField()


