from django.shortcuts import render
from polls.models import Company
from polls.services import validation
def index(request):
    return render(request, 'index.html')

def create(request):
    if(request.method == 'POST'):
        name = request.POST.get('inputNameCompany')
        spec = request.POST.get('inputSpecialityCompany')
        locate = request.POST.get('inputLocationCompany')

        if validation.isOptionHasCorrectLengthTo_50(name):
            return render(request, 'create.html', {'error_message': 'The name must '
                                                                    'be between 1 and 50 characters.'})
        if validation.isOptionHasCorrectLengthTo_100(spec):
            return render(request, 'create.html', {'error_message': 'The speciality must be '
                                                                    'between 1 and 100 characters.'})
        if validation.isOptionHasCorrectLengthTo_50(locate):
            return render(request, 'create.html', {'error_message': 'The locate must be between '
                                                                    '1 and 100 characters.'})
        try:
            obj = Company.objects.create(name=name, speciality=spec, locate=locate)
            obj.save()
        except ValueError:
            return render(request, 'create.html', {'error': 'Invalid input'})

    return render(request, 'create.html')

def list(request):
    # Логіка операції 2
    return render(request, 'list.html')

def delete(request):
    # Логіка операції 3
    return render(request, 'delete.html')

def update(request):
    # Логіка операції 4
    return render(request, 'update.html')

def details(request):
    # Логіка операції 5
    return render(request, 'details.html')