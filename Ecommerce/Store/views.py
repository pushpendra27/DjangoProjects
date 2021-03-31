from django.shortcuts import render
from .models.product import Product

# Create your views here.
def index(request):
    Fetched_product=Product.fetch_all_product()
    print(Fetched_product)
    
    return render(request,'index.html',{'product_':Fetched_product})
