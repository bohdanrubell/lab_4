from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createCompany/', views.createCompany, name='createCompany'),
    path('createEmployee/', views.createEmployee, name='createEmployee'),
    path('listCompany/', views.listCompany, name='listCompany'),
    path('listEmployee/', views.EmployeeListView.as_view(), name='listEmployee'),
    path('update_company/<int:company_id>/', views.update_company, name='update_company'),
    path('delete_company/<int:company_id>/', views.delete_company, name='delete_company'),
    path('update_employee/<int:employee_id>/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]
