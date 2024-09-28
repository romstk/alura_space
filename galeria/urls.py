from django.urls import path
from galeria.views import index, imagem, buscar

#Criamos uma lista que será responsável por gerenciar as rotas/urls do app galeria para exibir a view correspondente 
urlpatterns = [
        path('', index, name= 'home'),
        path('imagem/<int:foto_id>', imagem, name='imagem'),
        path('buscar', buscar, name="buscar")
]
