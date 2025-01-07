from django.urls import path
from usuarios.views import login, cadastro


#Criamos uma lista que será responsável por gerenciar as rotas/urls do app usuários para exibir a view correspondente 
urlpatterns = [
        path('login', login, name= 'login'),
        path('cadastro', cadastro, name= 'cadastro')
]
