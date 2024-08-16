from django.urls import path
from galeria.views import index, imagem

#Criamos uma lista que será responsável por gerenciar as rotas/urls do app galeria
urlpatterns = [
        path('', index, name= 'home'),
        path('imagem/', imagem, name='imagem')
]
