from django.urls import path
from galeria.views import index

#Criamos uma lista que será responsável por gerenciar as rotas/urls do app galeria
urlpatterns = [
        path('', index)
]
