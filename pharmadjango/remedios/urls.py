from django.urls import path
from . import views

urlpatterns = [
    path("listamedicamentos", views.lista_medicamentos, name="lista_medicamentos"),
]