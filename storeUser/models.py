from django.db import models
from owner.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=100,default=1)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")

