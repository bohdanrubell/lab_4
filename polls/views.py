from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from polls.forms import CompanyForm, EmployeeForm
from polls.models import Company, Employee
from polls.services import validation


def index(request):
    return render(request, 'index.html')


# @csrf_exempt
def createCompany(request):
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
    print(f"Request POST: {request.POST}")
    companies = Company.objects.all()
    form = EmployeeForm(initial={'company': companies})
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            salary = form.cleaned_data['salary']

            obj = Employee(company=company, name=name, position=position, salary=salary)
            obj.save()
    else:
        form = EmployeeForm()
    return render(request, 'createEmployee.html',
                  {'companies': Company.objects.all(),
                   'form': form})


def list(request):
    success_message = request.session.pop('success_message', None)
    employees = Employee.objects.all()
    companies = Company.objects.all()
    if success_message:
        return render(request, 'list.html',
                      {'success_message': success_message,
                       'employees': employees,
                       'companies': companies})
    else:
        return render(request, 'list.html',
                      {'employees': employees,
                       'companies': companies})


def details(request):
    return render(request, 'details.html')


def update_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            success_message = "The company was successfully updated."
            request.session['success_message'] = success_message
            return redirect('list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_update.html', {'formCompany': form})


def delete_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        company.delete()
        success_message = "The company was successfully deleted."
        request.session['success_message'] = success_message
        return redirect('list')  # Перенаправляем на страницу списка сотрудников
    return render(request, 'delete_company.html', {'company': company})
