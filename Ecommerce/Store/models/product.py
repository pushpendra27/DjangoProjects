from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,default='', null=True,blank=True)
    image=models.ImageField(upload_to='uplod/products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)#ForeignKey Delete All Category Tables


    @staticmethod
    def fetch_all_product():
        return Product.objects.all()
   


   