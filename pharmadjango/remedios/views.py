from django.shortcuts import redirect, render
from .models import Remedio
from django.contrib.auth import authenticate, login
from django.contrib import messages
import re


def lista_medicamentos_func(request):
    """lista todos os medicamentos cadastrados

        Args:
            request (request): requisição do usuário

    """
    remedios = Remedio.objects.all()
    context = {'remedios': remedios}
    return render(request, 'remedios/view_func.html', context)


def lista_medicamentos_admin(request):
    """lista todos os medicamentos cadastrados

        Args:
            request (request): requisição do usuário

    """
    remedios = Remedio.objects.all()
    context = {'remedios': remedios}
    return render(request, 'remedios/view_admin.html', context)


def lista_medicamentos_cliente(request):
    """lista todos os medicamentos cadastrados

        Args:
            request (request): requisição do usuário

    """
    remedios = Remedio.objects.all()
    context = {'remedios': remedios}
    return render(request, 'remedios/view_cliente.html', context)


def cadastra_medicamentos(request):
    """
    Cadastra os medicamentos no banco de dados

    """
    if request.method == "POST":
        nome = request.POST["nome"]
        preco = request.POST["preco"]
        tarja = request.POST["tarja"]
        receita = request.POST["receita"]

        # Verifica se o preço é float
        if preco != float:
            preco = re.sub(r'[^0-9.,]', '', preco)
            if ',' in preco:
                preco = preco.replace(',', '.')
            preco = float(preco)

        Remedio.objects.create(nome=nome, tarja=tarja, precisa_receita=receita, preco=preco)

    return render(request, "remedios/cadastro.html")


def logar(request):

    if request.method == "POST":
        username = request.POST["usuario"]
        passw = request.POST["senha"]
        user = authenticate(request, username=username, password=passw)

        if user is not None:
            if username == "admin":
                return redirect("/listamedicamentosadmin")

            login(request, user)
            return redirect("/listamedicamentosfunc")

        else:
            messages.success(request, ("Usuário ou senha incorretos"))
            return redirect("/login")

    else:

        return render(request, "remedios/login.html", {})


def deletar(request, remedio_id):
    remedio = Remedio.objects.get(pk=remedio_id)
    remedio.delete()

    return redirect("/listamedicamentosfunc")


def adicionar_carrinho(request, remedio_id):
    remedio = Remedio.objects.get(pk=remedio_id)

    context = {"remedio": remedio}

    return render(request, "remedios/carrinho.html", context)