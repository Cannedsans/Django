from .views import mlogin, signup, home,mlogout
from django.urls import path

urlpatterns = [
    path('login/', mlogin, name='login'),
    path('signup/',  signup, name='cadastro'),
    path('', home),
    path('sair/', mlogout, name="sair"),
]
