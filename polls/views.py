from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from polls.forms import CompanyForm, EmployeeForm
from polls.models import Company
from polls.services import validation


def index(request):
    return render(request, 'index.html')


# @csrf_exempt
def createCompany(request):
    print(f"Request POST: {request.POST}")
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            speciality = form.cleaned_data['speciality']
            locate = form.cleaned_data['locate']
            if Company.objects.filter(name=name).exists():
                return render(request, 'createCompany.html',
                              {'exist__error': 'The company already exists.', 'form': form})
            obj = Company.objects.create(name=name, speciality=speciality, locate=locate)
            obj.save()
            return render(request, 'createCompany.html',
                          {'success_message': 'The company was successfully added', 'form': form})
        else:
            errors = form.errors
            return render(request, 'createCompany.html', {'form': form, 'errors': errors})
    else:
        form = CompanyForm()
    return render(request, 'createCompany.html', {'form': form})


def createEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            salary = form.cleaned_data['salary']
    else:
        form = EmployeeForm()
    return render(request, 'createEmployee.html',
                  {'companies': Company.objects.all(),
                           'form': form})


def list(request):
    return render(request, 'list.html')


def delete(request):
    return render(request, 'delete.html')


def update(request):
    return render(request, 'update.html')


def details(request):
    return render(request, 'details.html')
