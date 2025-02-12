from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),

    path('livros/', views.livros, name='livros'),
    path('livros/criar/', views.criar_livro, name='criar_livro'),

    path('autores/', views.autores, name='autores'),
    path('autores/criar/', views.criar_autor, name='criar_autor'),

    path('clientes/', views.clientes, name='clientes'),
    path('clientes/criar/', views.criar_cliente, name='criar_cliente'),

    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('emprestimos/criar/', views.criar_emprestimo, name='criar_emprestimo'),
]
