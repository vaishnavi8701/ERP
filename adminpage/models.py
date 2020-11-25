from django.db import models

department = (
    ('Human Resource','Human Resource'),
    ('Technical','Technical'),
    ('Marketing','Marketing'),
    ('Finance', 'Finance'),
   
    
)

class addemployee(models.Model):
    image = models.ImageField(upload_to='pics', default = 'pics/person.png')
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    pan = models.CharField(max_length=20)
    whrs = models.IntegerField()
    oemail = models.EmailField(max_length=254)
    pemail = models.EmailField(max_length=254)
    designation = models.CharField(max_length=100)
    dept = models.CharField(max_length=100,choices=department, default='Human Resource')
    Gender = models.CharField(max_length=100)
    doj = models.DateField()
    address = models.TextField()
    job_loc = models.TextField()
    bank_name = models.CharField(max_length=100)
    ba_no = models.BigIntegerField()
    pfno = models.CharField(max_length=25)
    salary = models.IntegerField()
    Employee_id = models.CharField(max_length=25)
    msg= models.CharField(max_length=25)

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
 
class discount(models.Model):
    dis_per=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()
    service_id = models.CharField(max_length=100)
       
class addservices(models.Model):
  service_id = models.CharField(max_length=100)
  service_name = models.CharField(max_length=100, choices=service_name, default='window')
  category=models.CharField(max_length=100, choices=category, default='ERP')
  cost=models.IntegerField()
  technology=models.CharField(max_length=100, choices=technology, default='Python')

announce_to=(
    ('All','All'),
    ('HR','Human Resource'),
    ('Technical','Technical'),
    ('Marketing','Marketing'),
    ('Finance','Finance'),
)

class announcement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    announce_to=models.CharField(max_length=20,choices=announce_to,default='All')
    announce_by=models.CharField(max_length=20)
    message=models.TextField()

