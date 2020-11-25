from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile= models.CharField(max_length=15)
    aadhar = models.CharField(max_length=12)
    pan = models.CharField(max_length=20)
    whrs = models.IntegerField()
    oemail = models.EmailField(max_length=254)
    pemail = models.EmailField(max_length=254)
    designation = models.CharField(max_length=100)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    Gender = models.CharField(max_length=100)
    doj = models.DateField()
    address = models.CharField(max_length=1000)
    job_loc = models.CharField(max_length=1000)
    bank_name = models.CharField(max_length=100)
    ba_no = models.CharField(max_length=100)
    pfno = models.CharField(max_length=25)
    salary = models.CharField(max_length=15)