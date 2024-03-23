from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('createCompany/', views.createCompany, name='createCompany'),
    path('createEmployee/', views.createEmployee, name='createEmployee'),
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('details/', views.details, name='details'),
]
