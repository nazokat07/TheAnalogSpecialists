from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Repair
from django.http import Http404 

def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def sale(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(
        request,
        'main/sale.html',
        context
    )

def sale_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'error/404.html')
    #product = get_object_or_404(Product, id=pk)
    context = {
        'product':  product
    }
    return render(request, 'main/sale_detail.html', context)


def repairs(request):
    repairs = Repair.objects.all()
    context = {
        'repairs': repairs
    }
    return render(request, 'main/repairs.html', context)

def contact(request):
    return render(request, 'main/contact.html')
