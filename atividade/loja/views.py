from django.shortcuts import render
from .models import Produto,Vendedor
# Create your views here.

def index(request):
    return render(request,'index.html')

def produtos(request):
    produtos = Produto.objects.all()
    return render(request,'produtos.html',{'produtos': produtos})

def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request,'vendedores.html',{'vendedores': vendedores})
