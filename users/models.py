from django.db import models

# Create your models here.
# User model
class User(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=500)

    profile_pic = models.ImageField(upload_to='profile_pics', default=None)
    profil_bio = models.TextField(max_length=500, default="")


    score = models.IntegerField(default=0)

    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Favorite(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    postID = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username + ":" + self.postID
