from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) #one user can have one profile
    dob=models.DateField(null=True)
    options=(
        ("male","male"),
        ("female","female")
    )
    gender=models.CharField(max_length=50,choices=options)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    bio=models.CharField(max_length=200,null=True)
    cover_pic=models.ImageField(upload_to="coverpics",null=True)
    followings=models.ManyToManyField(User,related_name="following") #manytomany - user can follow so many users
    #related name shoud be given if in same class we give User model

class Posts(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    image=models.ImageField(upload_to="postimages",null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="liked_by")
    #we can only add image field later in models after migrations, foreign,onetoone cant be added

    def __str__(self):
        return self.title

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)


