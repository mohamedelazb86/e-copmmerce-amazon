from rest_framework import generics
from .models import Product
from .serializers import ProductDetailSerailizers,ProductListSerializers
from rest_framework.permissions import IsAuthenticated


class ProductApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializers

class ProductDetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerailizers
    permission_classes = [IsAuthenticated]