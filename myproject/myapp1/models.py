from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField(unique=True)
    password=models.CharField(max_length=20)
    profile = models.ImageField(default="",upload_to='profile/')
    
    def __str__(self):
        return self.name 