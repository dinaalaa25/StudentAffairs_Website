
from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainPage, name='MainPage'),
    path('Home', views.Home, name='Home'),
    path('AddStudent', views.AddStudents, name='Addstudent'),
    path('ViewStudent', views.ViewStudents, name='ViewStudent'),
    path('Search', views.Search, name='Search'),
    path('Edit/<int:id>', views.Edit, name='Edit'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('AssignDepartment/<int:id>',
         views.AssignDepartment, name='AssignDepartment'),
    path('delete/<int:id>', views.delete, name='delete'),

    path('activeStudent', views.activeStudent, name='activeStudent'),

]
