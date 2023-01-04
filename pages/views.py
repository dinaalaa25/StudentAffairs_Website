#from ast import Add
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

import pkg_resources
from .models import login
from .models import AddStudentt

# Create your views here.


def delete(request, id):
    member = AddStudentt.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('ViewStudent'))


def Home(request):
    return render(request, 'pages/Homepage.html')


def AddStudents(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        St_ID = request.POST.get('St_ID')
        dateofbirth = request.POST.get('dateofbirth')
        gpa = request.POST.get('gpa')
        Gender = request.POST.get('Gender')
        level = request.POST.get('level')
        status = request.POST.get('status')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        data = AddStudentt(fname=fname, lname=lname, dateofbirth=dateofbirth,
                           St_ID=St_ID, gpa=gpa, email=email, phonenumber=phonenumber, Gender=Gender, level=level, department=department, status=status)

        data.save()

    return render(request, 'pages/AddStudents.html')


def Search(request):
    if 'fname' in request.GET:
        name = request.GET['fname']
        students = AddStudentt.objects.filter(fname__icontains=name)
    else:
        students = AddStudentt.objects.all()
    return render(request, 'pages/Search.html', {'students': students})


def Edit(request, id):
    edit = AddStudentt.objects.get(id=id)
    if request.method == 'POST':
        edit.fname = request.POST.get('fname', False)
        edit.lname = request.POST.get('lname', False)
        edit.St_ID = request.POST.get('St_ID', False)
        edit.dateofbirth = request.POST.get('dateofbirth', False)
        edit.gpa = request.POST.get('gpa', False)
        edit.Gender = request.POST.get('Gender', False)
        edit.level = request.POST.get('level', False)
        edit.status = request.POST.get('status', False)
        edit.email = request.POST.get('email', False)
        edit.phonenumber = request.POST.get('phonenumber', False)
        edit.save()
        return HttpResponseRedirect(reverse('ViewStudent'))
    else:
        edit.fname = request.POST.get('fname')
        edit.lname = request.POST.get('lname')
        edit.St_ID = request.POST.get('St_ID')
        edit.dateofbirth = request.POST.get('dateofbirth')
        edit.gpa = request.POST.get('gpa')
        edit.Gender = request.POST.get('Gender')
        edit.level = request.POST.get('level')
        edit.status = request.POST.get('status')
        edit.email = request.POST.get('email')
        edit.phonenumber = request.POST.get('phonenumber')
    return render(request, 'pages/Edit.html', {'edit': edit})


def MainPage(request):
    return render(request, 'pages/MainPage.html')


def SignIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        data = login(email=email, password=password)
        data.save()
        return HttpResponseRedirect(reverse('Home'))

    return render(request, 'pages/SignIn.html')


def ViewStudents(request):
    ViewStudent = AddStudentt.objects.all()
    return render(request, 'pages/ViewStudents.html',
                  {'ViewStudent': ViewStudent})


def activeStudent(request):
    activeStudent = AddStudentt.objects.all()
    return render(request, 'pages/activeStudent.html',
                  {'activeStudent': activeStudent})


def AssignDepartment(request, id):
    edit = AddStudentt.objects.get(id=id)
    if request.method == 'POST':
        edit.department = request.POST.get('department')
        edit.save()
        return HttpResponseRedirect(reverse('activeStudent'))
    return render(request, 'pages/AssignDepartment.html')
