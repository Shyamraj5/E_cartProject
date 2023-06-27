from django.db import models
from owner.models import Product
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")
    @property
    def totel(self):
        
        cnt=(self.product.pr_price)
     
        return cnt
    def calculate_total_price(self):
        return self.cartitem_set.aggregate(total=models.Sum('product__price'))['total']
    