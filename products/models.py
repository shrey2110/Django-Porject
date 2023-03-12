from django.db import models
from django.contrib.auth.models import User
from Vendor.models import *

# Create your models here.
CATEGORY=(('','Select Your Category'),
          ('Vegetables','Vegetables'),
          ("Fruits","Fruits"),
          ("Dry-Fruits","Dry-Fruits"),
          ("Beverages","Beverages")
    
)

class products(models.Model):
    vendor=models.ForeignKey(User,on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to="products",null=True)
    product_category=models.CharField(max_length=100,choices=CATEGORY,null=True)
    MFG_Date=models.DateTimeField(auto_now_add=True,null=True)
    stock=models.IntegerField(null=True)
    piece=models.IntegerField(null=True)
    product_old_price=models.IntegerField(null=True)


    def __str__(self):
        return self.product_name