from django import forms
from .models import Livro, Autor, Cliente, Emprestismo
from datetime import datetime, timedelta

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'sub_titulo', 'genero', 'autor']
        
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), empty_label="Selecione um Autor")

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'sobrenome', 'nacionalidade', 'biografia']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'sobrenome', 'idade', 'endereco']

class EmprestismoForm(forms.ModelForm):
    class Meta:
        model = Emprestismo
        fields = ['idlivro', 'idcliente', 'data_emprestimo', 'data_devolucao']
    
    idlivro = forms.ModelChoiceField(queryset=Livro.objects.all(), empty_label="Selecione um Livro")
    idcliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Selecione um Cliente")

    data_emprestimo = forms.DateField(initial=datetime.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    data_devolucao = forms.DateField(initial=lambda: (datetime.today() + timedelta(days=15)).date(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))

