from django.shortcuts import render
from django.http import HttpResponse
from .models import Remedio
from django.template import loader

def lista_medicamentos(request):
    """lista todos os medicamentos cadastrados

        Args:
            request (request): requisição do usuário

    """
    remedios = Remedio.objects.all()
    context = {'remedios': remedios}
    return render(request, 'remedios/index.html', context)


def cadastra_medicamentos(request):
    """
    Cadastra os medicamentos no banco de dados

    """
    if request.method=="POST":
        nome = request.POST["nome"]
        preco = request.POST["preco"]
        tarja = request.POST["tarja"]
        receita = request.POST["receita"]
        Remedio.objects.create(nome=nome, tarja=tarja, precisa_receita=receita, preco=preco)
        
    return render(request, "remedios/cadastro.html")