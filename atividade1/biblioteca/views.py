from django.shortcuts import render, redirect
from .models import Livro, Autor, Cliente, Emprestismo
from .forms import LivroForm, AutorForm, ClienteForm, EmprestismoForm

def index(request):
    return render(request, 'index.html')

def livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros')
    else:
        form = LivroForm()
    return render(request, 'form_livro.html', {'form': form})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm()
    return render(request, 'form_autor.html', {'form': form})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'form_cliente.html', {'form': form})

def emprestimos(request):
    emprestimos = Emprestismo.objects.all()
    return render(request, 'emprestimos.html', {'emprestimos': emprestimos})

def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestismoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimos')
    else:
        form = EmprestismoForm()
    
    return render(request, 'form_emprestimo.html', {'form': form})
