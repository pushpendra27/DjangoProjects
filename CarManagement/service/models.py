from django.db import models

# Create your models here.
class Cars(models.Model):
    SERVICE_CHOICES=[('P','Platinum'),('G','Gold')]  #For Choices Selection
    car_model=models.CharField(max_length=100)
    car_owner=models.CharField(max_length=100)
    car_notes=models.CharField(max_length=100)
    car_number=models.CharField(max_length=30)
    description=models.TextField()
    service_type=models.CharField(choices=SERVICE_CHOICES,max_length=1,blank=True)
    submission_date=models.DateTimeField()
    years_old=models.IntegerField(null=True)#Less then a Year of Car 
    service=models.ManyToManyField('car_service',blank=True) #Many2Many 

class car_service(models.Model):
    name=models.CharField(max_length=50)    