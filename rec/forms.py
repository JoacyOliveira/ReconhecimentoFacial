from django.forms import ModelForm
from .models import Imagem

class ImagemForm(ModelForm):
    class Meta:
        model = Imagem
        fields = ['image']
