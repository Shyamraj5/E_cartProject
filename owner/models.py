from django.db import models

# Create your models here.

class Product(models.Model):
    pr_name=models.CharField(max_length=100)
    pr_price=models.IntegerField()
    options=(
        ('electronics','electronics'),
        ('food','food'),
        ('fashion','fashion'),
        ('home applianses','home applianses'),
        ('furniture','furniture'),
        ('grocery','grocery')
        
    )
    category=models.CharField(max_length=100,choices=options,default='')
    image=models.ImageField(upload_to="productImage")
    pr_discription=models.CharField(null=True, max_length=1000)