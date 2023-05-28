from django.urls import path
from . import views

urlpatterns = [
    path("listamedicamentosfunc", views.lista_medicamentos_func, name="lista_medicamentos_func"),
    path("listamedicamentosadmin", views.lista_medicamentos_admin, name="lista_medicamentos_admin"),
    path("listamedicamentoscliente", views.lista_medicamentos_cliente, name="lista_medicamentos_cliente"),
    path("cadastramedicamentos", views.cadastra_medicamentos, name="cadastra_medicamentos"),
    path("deletamedicamento/<remedio_id>", views.deletar, name="deletar"),
    path("adicionarcarrinho/<remedio_id>", views.adicionar_carrinho, name="adicionar"),
    path("login", views.logar, name="logar"),
]