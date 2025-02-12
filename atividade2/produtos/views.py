from django.shortcuts import render,get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    return render(request, "index.html" ,{"produtos": produtos})

def adicionar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o produto no banco de dados
            return redirect('index')  # Redireciona para a lista de produtos (você pode ajustar para onde redirecionar)
    else:
        form = ProdutoForm()

    return render(request, 'adicionar_produto.html', {'form': form})

def deletar(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('index')