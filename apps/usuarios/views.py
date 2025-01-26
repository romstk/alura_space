from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages



def login(request):
    #instacia da classe LoginFrom
    form = LoginForms()

    if request.method == 'POST': 
       #puxando os dados do formulário postado para uma variável.
       form = LoginForms(request.POST)

       #validando o formulário
       if form.is_valid():
         nome = form["nome_login"].value()
         senha = form["senha"].value()
       #neste ponto faremos a validação do usuário passando para um método do Django que fará a autenticação
       usuario = auth.authenticate(
           request, 
           username=nome,
           password=senha
        ) 
       #se o usuário for válido passo os parâmetros request e o usuário que vamos autenticar
       if usuario is not None:
           auth.login(request, usuario)
           messages.success(request, "Usuário logado com sucesso! ")
           return redirect('home')
       else:
           messages.error(request, "erro ao efetuar login")
           return redirect('login')
            
    #Ao renderizar o template passamos um dicionário com o objeto de form instanciado
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    #testamos qual o método que chamou esta view, se for post vamos executar a ação de armazenar os dados cadastrados. 
    if request.method == 'POST': 
        #armazeno os dados do formulário enviados por post na variável form
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            #atribuindo as variáveis com dados dos campos do forms.
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()

            #vamos testar agora se o usuário a ser cadastrado já existe, se existir redireciona para a página de cadastro novamente para cadastrar novo usuário
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente. ")
                return redirect('cadastro')
            
            #após todas as validações crio um novo usuário de fato
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Usuário cadastrado com sucesso. Já pode fazer o login. ")
            return redirect('login')

    #este return vai ser chamado somente se o método do request for diferente de POST, ou seja, se o formulário for chamado para cadastrar novo usuário 
    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.info(request, "Logout efetuado! ")
    return redirect('login')
