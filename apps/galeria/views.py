from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForm
from django.contrib.auth.decorators import login_required



#este decorator está definindo que esta view só será renderizada se o login tenha sido feito. Vou deixar ele comentado pois tenho um controle na aplicação com outro login que não é pelo github,que já bloqueia o acesso a páginas se não tiver feito login. 
#@login_required
def index(request):
    #primeiramente vamos testar se o usuário está logado. Se não tiver vamos redirecionar para login 
    if not request.user.is_authenticated: 
        messages.error(request, 'Usuário deve estar logado para acessar. ')
        return redirect('login')

    #criando um objeto que vai trazer os dados do banco de dados através de models.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    #vamos capturar o objeto do banco de dados com base no id(pk->primary key) recebido pela url.
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    #ao renderizar passo além da url passo um dicionário com os dados da fotografia
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    #primeiramente vamos testar se o usuário está logado. Se não tiver vamos redirecionar para login 
    if not request.user.is_authenticated: 
        messages.error(request, 'Usuário deve estar logado para acessar. ')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET: 
        nome_a_buscar = request.GET["buscar"] 
        if nome_a_buscar:
            #vamos redefinir fotografias com o filtro da variável nome__icontains quer dizer que estamos buscando na variável nome se contém o nome a buscar em alguma parte dete 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
        #aqui passamos para o template buscar.html os cards que é um dicionário com os dados filtrados.
        return render(request, 'galeria/buscar.html',{"cards": fotografias})
    

def nova_imagem(request):
    if not request.user.is_authenticated: 
        messages.error(request, 'Usuário deve estar logado para acessar. ')
        return redirect('login')
    #se o método for GET vai pular para última linha, levando para o form de inclusão de nova imagem
    form = FotografiaForm() 
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() #como estamos usando um ModelForm-FotografiaForm já basta mandar o form ser salvo que o Django se encarrega de tratar a model vinculada ao form e salvar os dados. 
            messages.success(request, 'Nova fotografia cadastgrada')
            return redirect('home')


    return render(request, 'galeria/nova_imagem.html', {'form':form})


def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass