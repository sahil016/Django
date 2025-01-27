from django.db import models

# Create your models here.

class User(models.Model):
    usertype=models.CharField(max_length=20,default="buyer")
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField(unique=True)
    password=models.CharField(max_length=20)
    profile = models.ImageField(default="",upload_to='profile/')
    
    def __str__(self):
        return self.name 
    
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete= models.CASCADE)
        
    category = (
        ("Men", "Men"),
        ("Women", "Women"),
        ("Kids", "Kids"),
    )

    brand = (
        ("Raymond", "Raymond"),
        ("Levis", "Levis"),
        ("Puma", "Puma"),
        ("Nike", "Nike"),
        ("Adidas", "Adidas"),
    )

    size = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    )
    scategory = models.CharField(max_length=40,choices=category)
    sbrand = models.CharField(max_length=40,choices=brand)
    ssize = models.CharField(max_length=40,choices=size)
    pname = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    
    def __str__(self):
        return self.pname
    
    
class Cart(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    total = models.IntegerField (default=0)
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)