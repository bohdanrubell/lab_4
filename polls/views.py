from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def operation1(request):
    # Логіка операції 1
    return render(request, 'operation1.html')

def operation2(request):
    # Логіка операції 2
    return render(request, 'operation2.html')

def operation3(request):
    # Логіка операції 3
    return render(request, 'operation3.html')

def operation4(request):
    # Логіка операції 4
    return render(request, 'operation4.html')

def operation5(request):
    # Логіка операції 5
    return render(request, 'operation5.html')