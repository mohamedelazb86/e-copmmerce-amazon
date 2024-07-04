from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,ProductImge,Brand,Review


class ProductImgesadmin(admin.TabularInline):
    model=ProductImge

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','sku','flag']
    search_fields=['name','subtitle','descriptions']
    list_filter=['flag','brand']
    inlines=[ProductImgesadmin]

    summernote_fields = ('subtitle','descriptions')

admin.site.register(Product,ProductAdmin)
#admin.site.register(ProductImge)
admin.site.register(Brand)
admin.site.register(Review)
