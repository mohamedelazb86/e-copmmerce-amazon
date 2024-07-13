from rest_framework import serializers
from .models import Post

class Post_ListSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'

class PostDetailSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'
class Post_update_delete_create(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
