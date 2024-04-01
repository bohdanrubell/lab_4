from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    speciality = models.CharField(max_length=20)
    locate = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    position = models.CharField(max_length=20)
    salary = models.SmallIntegerField(default=0)
    def __str__(self):
        return self.name