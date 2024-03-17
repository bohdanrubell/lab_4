from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('details/', views.details, name='details'),
]
