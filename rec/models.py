from django.db import models

# Create your models here.

class Imagem(models.Model):
    image = models.ImageField()

    def __str__(self):
        return str(self.image)

