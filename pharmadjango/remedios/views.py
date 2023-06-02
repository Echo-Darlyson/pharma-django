from django.shortcuts import redirect, render
from .models import Remedio, Carrinho
from django.contrib.auth import authenticate, login
from django.contrib import messages

import re
import json


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

        Remedio.objects.create(nome=nome, tarja=tarja, precisa_receita=receita, preco=preco)  # noqa: E501

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
            return redirect("/")

    else:

        return render(request, "remedios/login.html", {})


def deletar(request, remedio_id):
    remedio = Remedio.objects.get(pk=remedio_id)
    remedio.delete()

    return redirect("/listamedicamentosfunc")


def remover_remedio_carrinho(request, remedio_id):
    """Remove um remedio do carrinho

    Args:
        request (request): requisição do usuário
        remedio_id (int): id do remedio a ser removido

    """
    carrinho = Carrinho.objects.order_by("-id").first()

    if carrinho:
        items = json.loads(carrinho.remedios)
        ids_list = [item['id'] for item in items]
        if remedio_id in ids_list:
            remedio = Remedio.objects.get(pk=remedio_id)
            if remedio:
                items = [item for item in items if item['id'] != remedio_id]
                carrinho.remedios = json.dumps(items)
                carrinho.save()

    return redirect("exibir_carrinho")


def exibir_carrinho(request):
    """exibe o carrinho de compras

    Args:
        request (request): requisição do usuário

    """
    carrinho_db = Carrinho.objects.order_by("-id").first()

    options = None
    if carrinho_db:
        carrinho = carrinho_db.remedios
        items = json.loads(carrinho)
        options = []
        for item in items:
            try:
                remedio = Remedio.objects.get(pk=item['id'])
                options.append({
                    "id": remedio.id,
                    "nome": remedio.nome,
                    "preco": float(remedio.preco),
                    "tarja": remedio.tarja,
                    "precisa_receita": remedio.precisa_receita
                })
            except Remedio.DoesNotExist:
                options = [item for item in items if item['id'] != item['id']]
                carrinho_db.remedios = json.dumps(options)
                carrinho_db.save()

    context = {"remedios": options}

    return render(request, "remedios/carrinho.html", context)


def adicionar_carrinho(request, remedio_id):
    """Adiciona um remedio ao carrinho (caso já não o tenha)

    Args:
        request (request): requisição do usuário
        remedio_id (int): id do remedio a ser adicionado

    """
    carrinho = Carrinho.objects.order_by("-id").first()

    options = []
    if carrinho:
        items = json.loads(carrinho.remedios)
        ids_list = [item['id'] for item in items]
        if remedio_id not in ids_list:
            remedio = Remedio.objects.get(pk=remedio_id)
            items.append({
                "id": remedio.id,
                "nome": remedio.nome,
                "preco": float(remedio.preco),
                "tarja": remedio.tarja,
                "precisa_receita": remedio.precisa_receita
            })
            carrinho.remedios = json.dumps(items)
            carrinho.save()
    else:
        remedio = Remedio.objects.get(pk=remedio_id)
        options.append({
            "id": remedio.id,
            "nome": remedio.nome,
            "preco": float(remedio.preco),
            "tarja": remedio.tarja,
            "precisa_receita": remedio.precisa_receita
        })
        Carrinho.objects.create(remedios=json.dumps(options), total=0)

    return redirect("exibir_carrinho")
