from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
def index(request): 
    #criando um objeto que vai trazer os dados do banco de dados através de models.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    #vamos capturar o objeto do banco de dados com base no id(pk->primary key) recebido pela url.
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    #ao renderizar passo além da url passo um dicionário com os dados da fotografia
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

