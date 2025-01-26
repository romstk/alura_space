from django.urls import path
from apps.galeria.views import \
        index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem

#Criamos uma lista que será responsável por gerenciar as rotas/urls do app galeria para exibir a view correspondente 
urlpatterns = [
        path('', index, name= 'home'),
        path('imagem/<int:foto_id>', imagem, name='imagem'),
        path('buscar', buscar, name="buscar"),
        path('nova-imagem', nova_imagem, name="nova_imagem"),
        path('editar-imagem', editar_imagem, name="editar_imagem"),
        path('deletar-imagem', deletar_imagem, name="deletar_imagem")
]
