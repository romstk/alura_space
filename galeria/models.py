from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Criação das classes de modelo que herdarão a classe models 
class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELIA", "Estrela"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    #campo associado a tabela de usuários para armazenarmos o usuário
    #on_delete - caso o usuário seja deletado vamos atribuir null a este campo
    #null=True, significa que o campo aceitará o valor null
    #related_name="user" , este campo serve para para facilitar a localização de tabelas e funcionalidades
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user" 
    )
    #para retornar somente o nome da classe 
    def __str__(self):
        return self.nome