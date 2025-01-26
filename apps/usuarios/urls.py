from django.urls import path
from apps.usuarios.views import login, cadastro, logout


#Criamos uma lista que será responsável por gerenciar as rotas/urls do app usuários para exibir a view correspondente 
urlpatterns = [
        path('login', login, name= 'login'),
        path('cadastro', cadastro, name= 'cadastro'),
        path('logout', logout, name='logout'),
]
