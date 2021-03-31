from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from datetime import datetime
from Application.models import Contact


# Create your views here.

def index(request):
    """
    context= {
        'variable':"This Is Sent Variable"
    }
    """

    #return render(request,'index.html',context)
    return render(request,'index.html')
def about(request):
    #return HttpResponse("<h1>Hey Pushpendra This is your About Pages</h1> ")
    return render(request,'about.html')
def service(request):
    #return HttpResponse("<h1>Hey Pushpendra This is your Service  Pages</h1> ")
    return render(request,'services.html')
def contact(request):
    #return HttpResponse("<h1>Hey Pushpendra This is your Contact Pages</h1> ")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,mobile=mobile,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
def order(request):
    #return HttpResponse("<h1>Hey Pushpendra This is your Order List Pages</h1> ")
    return render(request,'order.html')

"""
def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)

     name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
"""

