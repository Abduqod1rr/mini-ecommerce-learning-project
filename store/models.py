from django.db import models
from django.contrib.auth.models import User ,AbstractUser 
from django.conf import settings
from django.urls import reverse
from users.models import CustomUser 
# Create your models here.
    
class Category(models.Model):   
    name=models.CharField(max_length=60)
    slug=models.SlugField(unique=True)

    def __str__(self) :
        return self.name
    
class Product(models.Model):
    title=models.CharField(max_length=70)
    about=models.TextField(default="nothing")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField(default=0)
    image=models.ImageField(upload_to='products/')
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    is_active=models.BooleanField(default=True)
    seller=models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             related_name="products",
                             null=True,
                             blank=True
                             
                             )
    def __str__(self):
        return self.title , self.seller
    
class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.user.username
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"
    
class Order(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")

    def __str__(self) :
        return f"{self.user.username}-{self.status}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE) #tog'ri ketayapmanmi
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self) :
        return f"{self.product.title} x {self.quantity}"
 