from django.contrib import admin

from apps.galeria.models import Fotografia

#adiciono uma classe que vai herdar admin.ModelAdmin
#No escopo da classe, digitamos um parâmetro nomeado "list_display()" em que desejamos exibir o id, o nome e a legenda. 
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links= ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria", "usuario",)
    list_editable = ("publicada", )
    list_per_page = 10

#passamos para o método todas as classes que queremos registrar 
admin.site.register(Fotografia, ListandoFotografias)
