from django.urls import path
from .views import index,produtos,vendedores

urlpatterns = [
    path('', index, name= "home"),
    path('produtos/', produtos, name="produtos"),
    path('vendedores/', vendedores, name="vendedores"),

]
