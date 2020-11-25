from django.db import models
from marketing.models import client

# Create your models here.


ser = (
    ('Recharges','Recharges'),
    ('Electricity','Electricity' ),
    ('Building Rent','Building Rent'),
    ('Water Supply','Water Supply'),
    
)
pay = (
    ('Cash','Cash'),
    ('Cheque', 'Cheque'),
    ('Online','Online'),
 
    
)
time = (
    ('Weekly','Weekly'),
    ('Monthly', 'Monthly'),
    ('Fourthnight','Fourthnight'),
 
    
)
types= (
    ('Fixed','Fixed'),
    ('Variable', 'Variable'),
 
    
)

class vendor(models.Model):
    vendor_id=models.CharField(max_length=100)
    vendor_name=models.CharField(max_length=100)
    service_provided=models.CharField(max_length=100,choices=ser, default='Recharges')
    cost=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    due_date=models.DateField(auto_now_add=False)
    payment_duration=models.CharField(max_length=100,choices=time, default='Weekly')
    mode_of_pay=models.CharField(max_length=100,choices=pay, default='Cash')
    status=models.CharField(max_length=100)
    vendor_pan=models.CharField(max_length=100)
    vendor_gst=models.CharField(max_length=100)
    type_amt=models.CharField(max_length=100,choices=types, default='Fixed')
    bank_name=models.CharField(max_length=100)
    acc_no=models.CharField(max_length=100)
    paid_date=models.DateField(auto_now_add=False)
    pay_status=models.CharField(max_length=100)
    month=models.CharField(max_length=100)


class Receipt(models.Model):
    receipt_id=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    client_id=models.CharField(max_length=100)
    client_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    totalvalue=models.CharField(max_length=100)
    
    balance_amt=models.CharField(max_length=100)
    amount_received=models.CharField(max_length=100)
    next_duedate=models.DateField(auto_now_add=True)
    mode_of_pay=models.CharField(max_length=100)
    cheque=models.CharField(max_length=100)
    cheque_date=models.DateField(auto_now_add=True)
    tax=models.CharField(max_length=100)
    bank_name=models.CharField(max_length=100)
    online_ref=models.CharField(max_length=100)
    

class taxpayment(models.Model):
    client_id=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    receipt_id=models.CharField(max_length=100)
    sgst=models.CharField(max_length=100)
    cgst=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)
    
    

