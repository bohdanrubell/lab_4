from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('createCompany/', views.createCompany, name='createCompany'),
    path('createEmployee/', views.createEmployee, name='createEmployee'),
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('update_company/<int:company_id>/', views.update_company, name='update_company'),
    path('delete_company/<int:company_id>/', views.delete_company, name='delete_company'),
    path('details/', views.details, name='details'),
]
