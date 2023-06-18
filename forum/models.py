from django.db import models

# Create your models here.
class Post(models.Model):
    postID = models.AutoField(primary_key=True)

    status = models.IntegerField(default=0) # 0 = open, 1 = closed

    author = models.CharField(max_length=25)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=60, default="")
    subcategory = models.CharField(max_length=60, default="")

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    def __str__(self): 
        return str(self.postID) + " - '" + self.title + "' by " + self.author


class Comment(models.Model):
    commmentID = models.AutoField(primary_key=True)
    parentID = models.IntegerField(default=0)

    author = models.CharField(max_length=25)
    content = models.TextField(max_length=2500)
    date = models.DateTimeField(auto_now_add=True)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return  "Comment " + str(self.commmentID) + " to " + str(self.parentID)  + " by " + self.author