from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAutForm
# Create your views here.
def mlogin(request):
    if request.method == 'POST':
        form = CustomAutForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha incorretos")
    else:
        form = CustomAutForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')  
        else:
            messages.error(request, "Erro no cadastro. Verifique os dados.")
    else:
        form = UserCreationForm()

    return render(request, 'singup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'tela.html')

def mlogout(request):
    logout(request)
    return redirect('/')