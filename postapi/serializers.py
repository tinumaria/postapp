from rest_framework import serializers
from django.contrib.auth.models import User
from postapi.models import UserProfile,Posts,Comments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True) # - if we need name
    #user=UserSerializer(read_only=True) - if we need details

    class Meta:
        model=UserProfile
        fields=[
            "user",
            "gender",
            "bio",
            "profile_pic"
        ]
    def create(self, validated_data):
        user=self.context.get("user")
        return UserProfile.objects.create(user=user,**validated_data)

class PostSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)

    class Meta:
        model=Posts
        exclude=("liked_by",) #everything except like will come
        # , is given to make it tuple

class CommentSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model=Comments
        exclude=("date",)

    def create(self, validated_data):
        user=self.context.get("user")
        post=self.context.get("post")
        return Comments.objects.create(user=user,post=post,**validated_data)