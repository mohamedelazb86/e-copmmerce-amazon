from django.db import models
from taggit.managers import TaggableManager


from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
    ]
class  Product(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(max_length=50,choices=FLAG_TYPE)
    price=models.FloatField()
    image=models.ImageField(upload_to='photo_image')
    sku=models.IntegerField()
    subtitle=models.TextField(max_length=5000)
    descriptions=models.TextField(max_length=50000)
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    quantity=models.FloatField()

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)


class Brand(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    image=models.ImageField(upload_to='photo_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)

class ProductImge(models.Model):
    product=models.ForeignKey(Product,related_name='productimage_product',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)