from django.urls import path
from .views import cadastro,login,site

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('', site,name='site')
]
