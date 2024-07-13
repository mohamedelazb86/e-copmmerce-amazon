from rest_framework import generics
from .serializers import Post_ListSerializers,PostDetailSerializers,Post_update_delete_create
from .models import Post

class PostLiSTaPI(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_ListSerializers

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializers
    

class Post_update_Createapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_update_delete_create

    