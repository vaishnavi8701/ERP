from django.db import models
from adminpage.models import addemployee
# Create your models here.


class leave(models.Model):
    date = models.DateField(auto_now_add=True)
    leave_type=models.CharField(max_length=50)
    emp_name=models.CharField(max_length=100)
    emp_id=models.CharField(max_length=20)
    branch=models.CharField(max_length=100)
    desgn=models.CharField(max_length=100)
    from_date=models.DateField(auto_now_add=False)
    to_date=models.DateField(auto_now_add=False)
    status=models.CharField(max_length=100)
    numdays=models.IntegerField()
    reason=models.TextField()

class OTP(models.Model):
    email=models.CharField(max_length=100)
    otp=models.IntegerField()

class salaryemp(models.Model):
    date_of_generate=models.DateField(auto_now_add=True)
    date_of_payment=models.DateField(auto_now_add=True)
    emp_name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    emid=models.CharField(max_length=100)
    present_days=models.IntegerField()
    sal=models.CharField(max_length=100)
    working_days=models.CharField(max_length=100)
    gross=models.CharField(max_length=100)
    pf=models.CharField(max_length=100)
    esi=models.CharField(max_length=100)
    it=models.CharField(max_length=100)
    total_dedu=models.CharField(max_length=100)
    payable=models.CharField(max_length=100)
    basic_pay=models.CharField(max_length=100)
    hra=models.CharField(max_length=100)
    special_allowance=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    month=models.CharField(max_length=100)
    acno=models.CharField(max_length=100)
 
   

class salmonth(models.Model):
    month=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)

