from rest_framework import serializers
from.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source="author.username",read_only=True)

    class Meta:
        model=Post
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'