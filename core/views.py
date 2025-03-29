from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def productos(request):
    return render(request, 'productos.html')

def producto(request):
    return render(request, 'producto.html')