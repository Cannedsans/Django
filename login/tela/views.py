from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Já existe um usuário com esse email.")
            return render(request, 'cadastro.html')

        oi = User.objects.create_user(username=nome, email=email)
        oi.set_password(senha)
        oi.save()
        messages.success(request, "Usuário criado com sucesso.")
        return render(request, 'cadastro.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(email=email)  # Encontra o usuário pelo email
            tu = authenticate(username=user.username, password=senha)
            if tu:
                auth_login(request, tu)  # Faz login na sessão
                return HttpResponse("Autenticado")
            else:
                return HttpResponse("Errou algo aí, rapá")
        except User.DoesNotExist:
            return HttpResponse("Usuário não encontrado")
        
@login_required
def site(resquest):
    return HttpResponse("SITE")