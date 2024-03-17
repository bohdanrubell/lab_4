from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('operation1/', views.operation1, name='operation1'),
    path('operation2/', views.operation2, name='operation2'),
    path('operation3/', views.operation3, name='operation3'),
    path('operation4/', views.operation4, name='operation4'),
    path('operation5/', views.operation5, name='operation5'),
]
