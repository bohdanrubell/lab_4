from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def create(request):
    # Логіка операції 1
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