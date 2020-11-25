from django.db import models

# Create your models here.

stat = (
    ('Opened','Opened'),
    ('Closed', 'Closed'),
   
    
)
service_name = (
    ('Window','Window Application'),
    ('Web', 'Web Application'),
    ('Network','Network Application'),
    ('Mobile','Mobile Application'),
    
)
category = (
    ('ERP','ERP'),
    ('CRM','CRM' ),
    ('Billing','Billing'),
    ('Ecommerce','Ecommerce'),
    ('HRM','HRM'),
    
)
technology = (
    ('Python','Python'),
    ('Php', 'Php'),
    ('Java','Java'),
    ('DotNet','DotNet'),
    
)
class client(models.Model):
    clientid=models.CharField(max_length=100)
    clientname=models.CharField(max_length=100)
    client_address=models.CharField(max_length=500)
    company_name=models.CharField(max_length=500)
    contact=models.CharField(max_length=10)
    alcontact=models.CharField(max_length=10)
    company_email= models.EmailField(max_length=254)
    meeting=models.CharField(max_length=100,choices=category, default='ERP')
    remarks=models.CharField(max_length=500)
    status=models.CharField(max_length=100,choices=stat, default='Opened')
    date=models.DateField(auto_now_add=True)
    empname=models.CharField(max_length=100)
    quotation=models.CharField(max_length=100)
    empid=models.CharField(max_length=100)
    total=models.CharField(max_length=100)

#receipts , payments ,quotation, project



technology = (
    ('Python','Python'),
    ('Php', 'Php'),
    ('Java','Java'),
    ('DotNet','DotNet'),
    
)

class Emp_Quot(models.Model):
    quotation_id=models.CharField(max_length=100)
    clientid=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)
    total=models.CharField(max_length=100)
    first_payment_date=models.DateField()
    reason=models.TextField()
    client_deadline=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    first_amt=models.CharField(max_length=100)
    client_name=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    tax=models.CharField(max_length=100) 
    subtotal=models.CharField(max_length=100)
    balance=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    second_amt=models.CharField(max_length=100)
    third_amt=models.CharField(max_length=100)
    second_payment_date=models.DateField()
    third_payment_date=models.DateField()
    executive=models.CharField(max_length=100)
    project_status=models.CharField(max_length=100)
    source_code=models.FileField(upload_to="source")
    project_end_date=models.DateField(auto_now_add=True)
    project_start_date=models.DateField(auto_now_add=True)
    project_leader=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    work=models.BooleanField()
    accept=models.CharField(max_length=100)
    date_of_complete=models.DateField(auto_now_add=True)



class services_quot(models.Model):
    service_id=models.CharField(max_length=100)
    quotation_id=models.CharField(max_length=100)
    service_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    no_of_units=models.IntegerField()
    tax_percent=models.CharField(max_length=100)
    total=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    technology=models.CharField(max_length=100)
    clientid=models.CharField(max_length=100)
  
