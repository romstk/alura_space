from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    #instacia da classe LoginFrom
    form = LoginForms()
    #Ao renderizar o template passamos um dicionário com o objeto de form instanciado
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": form})

