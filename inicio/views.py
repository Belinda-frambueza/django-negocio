from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


def index(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()

    productos = Producto.objects.all().order_by('-id')
    return render(request, 'index.html', {'form': form, 'productos': productos})


def nosotros(request):
    return render(request, 'nosotros.html')