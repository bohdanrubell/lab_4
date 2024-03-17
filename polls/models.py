from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    locate = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name