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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['company'].empty_label = '---SELECT---'
        self.fields['company'].queryset = Company.objects.all()
