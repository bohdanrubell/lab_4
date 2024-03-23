# forms.py
from django import forms
from .models import Company, Employee


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'speciality', 'locate')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of company'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control'}),
            'locate': forms.TextInput(attrs={'class': 'form-control'})
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('company', 'name', 'position', 'salary')

        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'})
        }
