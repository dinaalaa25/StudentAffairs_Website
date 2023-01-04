from email.policy import default
from random import choices
from django.db import models
from django.utils import timezone

# Create your models here.
class login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class AddStudentt(models.Model):
    gender_choices=[('female','Female'),('male','Male')]
    level_choices = [
        ('one' , 'one'),
        ('two' , 'two'),
        ('three' ,'three'),
        ('four' , 'four'),
    ]
    status_choices = [
        ('active','Active'),
        ('inactive','In Active'),
    ]
    department_choices=[
        ('general','General'),
        ('is','Information System'),
        ('cs','Computer Science'),
        ('ai','Artificial Intelligence'),
        ('ds','Decision Support'),
        ('it','Information Tecnology'),
    ]


    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dateofbirth = models.DateTimeField(auto_now_add=True)
    St_ID = models.IntegerField(null=False)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True ,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    phonenumber=models.IntegerField(null=True)
    Gender=models.CharField(max_length=50,choices=gender_choices,null=True,blank=True)
    level=models.CharField(max_length=50,choices=level_choices,null=True,blank=True)
    status=models.CharField(max_length=50,choices=status_choices,null=True,blank=True)
    department=models.CharField(max_length=50,choices=department_choices,null=True,blank=True)

   