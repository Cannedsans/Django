from django.urls import path
from .views import index, adicionar, deletar

urlpatterns = [
    path('', index, name="index"),
    path('adicionar/', adicionar, name='adicionar_produto'),
    path('apagar/<int:produto_id>/', deletar, name='apagar_produto'),
]
