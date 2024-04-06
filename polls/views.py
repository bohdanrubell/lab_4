from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from polls.forms import CompanyForm, EmployeeForm
from polls.models import Company, Employee
from polls.services import companyManager, employeeManager
from django.views.generic import ListView, View


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
                              {'exist__error': 'The company already exists. Please create another', 'form': form})

            companyManager.createCompany(name=name, speciality=speciality, locate=locate)
            return render(request, 'createCompany.html',
                          {'success_message': 'The company was successfully added', 'form': form})
        else:
            errors = form.errors
            return render(request, 'createCompany.html', {'form': form, 'errors': errors})
    else:
        form = CompanyForm()
    return render(request, 'createCompany.html', {'form': form})


def createEmployee(request):
    companies = Company.objects.all()
    form = EmployeeForm(initial={'company': companies})
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            salary = form.cleaned_data['salary']
            if not employeeManager.isHasRightSalary(salary):
                return render(request, 'createEmployee.html', {'form': form,
                                                               'exist__error': "The salary isn't correct,"
                                                                               "please try again(from 1 to 100000$)"})

            if employeeManager.ifExists(company=company, name=name, position=position,salary=salary):
                return render(request, 'createEmployee.html',
                          {'exist__error': 'The employee already exists. Please create another', 'form': form})
            employeeManager.createEmployee(company=company, name=name, position=position,salary=salary)
            return render(request, 'createEmployee.html', {'success_message': 'The employee was successfully added', 'form': EmployeeForm()})
    else:
        form = EmployeeForm()
    return render(request, 'createEmployee.html',
                  {'companies': Company.objects.all(),
                   'form': form})

def update_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            success_message = "The company was successfully updated."
            request.session['success_message'] = success_message
            return redirect('listCompany')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_update.html', {'formCompany': form})


def delete_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        company.delete()
        success_message = "The company was successfully deleted."
        request.session['success_message'] = success_message
        return redirect('listCompany')
    return render(request, 'delete_company.html', {'company': company})

def listCompany(request):
    success_message = request.session.pop('success_message', None)
    companies = Company.objects.all()
    return render(request, 'listCompany.html',
                  {'companies': companies,
                   'success_message': success_message})


class EmployeeListView(ListView):
    model = Employee
    template_name = 'listEmployee.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_message'] = self.request.session.pop('success_message', None)
        return context



class EmployeeUpdateView(View):
    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        form = EmployeeForm(instance=employee)
        return render(request, 'employee_update.html', {'formEmployee': form})

    def post(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            if not employeeManager.isHasRightSalary(form.cleaned_data['salary']):
                return render(request, 'employee_update.html', {'formEmployee': EmployeeForm(instance=employee),
                                                                'exist_error': "The salary isn't correct, "
                                                                               "please try again (from 1 to 100000$)"})
            form.save()
            success_message = "The employee was successfully updated."
            request.session['success_message'] = success_message
            return redirect('listEmployee')
        return render(request, 'employee_update.html', {'formEmployee': form})


def listEmployee(request):
    success_message = request.session.pop('success_message', None)
    employees = Employee.objects.all()
    return render(request, 'listEmployee.html',
                  {'employees': employees,
                   'success_message': success_message})


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            if not employeeManager.isHasRightSalary(form.cleaned_data['salary']):
                return render(request, 'employee_update.html', {'formEmployee': EmployeeForm(instance=employee),
                                                               'exist__error': "The salary isn't correct,"
                                                                               "please try again(from 1 to 100000$)"})
            form.save()
            success_message = "The employee was successfully updated."
            request.session['success_message'] = success_message
            return redirect('listEmployee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {'formEmployee': form})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        success_message = "The employee was successfully deleted."
        request.session['success_message'] = success_message
        return redirect('listEmployee')
    return render(request, 'delete_employee.html', {'employee': employee})