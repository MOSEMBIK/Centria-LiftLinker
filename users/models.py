from django.db import models

# Create your models here.
# User model
class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

