from optparse import Option
from ssl import Options
from tkinter import Widget
from django import forms

class AddStudent(forms.Form):
     gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
     level_choice = [
        ('one' , 'one'),
        ('two' , 'two'),
        ('three' ,'three'),
        ('four' , 'four'),
    ]

     status_choice = [
        ('active','Active'),
        ('inactive','In Active'),
    ]
     department_choice=[
        ('general','General'),
        ('is','Information System'),
        ('cs','Computer Science'),
        ('ai','Artificial Intelligence'),
        ('ds','Decision Support'),
        ('it','Information Tecnology'),
    ]
     firstname = forms.CharField(max_length=50)
     lastname = forms.CharField(max_length=50)
    # dateofbirth = forms.DateTimeField()
     St_ID = forms.IntegerField()
     gpa = forms.DecimalField(max_digits=3, decimal_places=2)
    
     gender = forms.ChoiceField (choices=gender_choice)
     level = forms.ChoiceField (choices=level_choice)
     status = forms.ChoiceField (choices=status_choice)
     department = forms.ChoiceField (choices=department_choice)
     email = forms.CharField(max_length=50)
     phonenumber = forms.IntegerField()

