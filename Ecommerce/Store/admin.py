from django.contrib import admin
# Manually Created Models
from .models.product import Product
from .models.category import Category



class productAdmin(admin.ModelAdmin):
    list_display=['name','price','category','description']


class categoryAdmin(admin.ModelAdmin):
    list_display=['name']


# Register your models here.

admin.site.register(Product,productAdmin)
admin.site.register(Category,categoryAdmin)