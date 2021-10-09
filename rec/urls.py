from django.urls import path
from .views import salvar_imagem

urlpatterns = [
    path('', salvar_imagem, name='home'),
]
