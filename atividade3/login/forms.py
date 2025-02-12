from django import forms 
from django.contrib.auth.forms import AuthenticationForm

class CustomAutForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do usuário"}),
        label="Nome do usuário"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Senha"}),
        label="Senha"
    )
