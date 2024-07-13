from rest_framework import serializers
from .models import Product,ProductImge


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductImge
        fields='__all__'

class ProductListSerializers(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields='__all__'

class ProductDetailSerailizers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    productimge=ProductImageSerializers(source='productimage_product',many=True)
    class Meta:
        model=Product
        fields='__all__'
