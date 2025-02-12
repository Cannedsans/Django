from django import forms
from .views import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']
        widgets = {
            'preco': forms.NumberInput(attrs={'step': 0.01}),
        }