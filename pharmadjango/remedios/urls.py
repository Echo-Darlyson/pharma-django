from django.urls import path
from . import views

urlpatterns = [
    path("listamedicamentosfunc", views.lista_medicamentos_func, name="lista_medicamentos_func"),  # noqa: E501
    path("listamedicamentosadmin", views.lista_medicamentos_admin, name="lista_medicamentos_admin"),  # noqa: E501
    path("listamedicamentoscliente", views.lista_medicamentos_cliente, name="lista_medicamentos_cliente"),  # noqa: E501
    path("cadastramedicamentos", views.cadastra_medicamentos, name="cadastra_medicamentos"),  # noqa: E501
    path("deletamedicamento/<remedio_id>", views.deletar, name="deletar"),
    path("removecarrinho/<int:remedio_id>", views.remover_remedio_carrinho, name="remover_remedio_carrinho"),  # noqa: E501
    path("exibircarrinho", views.exibir_carrinho, name="exibir_carrinho"),
    path("adicionarcarrinho/<int:remedio_id>", views.adicionar_carrinho, name="adicionar_carrinho"),  # noqa: E501
    path("", views.logar, name="logar"),
]
