from django.db import models

from datetime import datetime

class Fotografia(models.Model):
    OPCAO_CATEGORIA=[
        ('NEBULOSA', 'Nebulosa'),
        ('GALÁXIA', 'Galáxia'),
        ('ESTRELA', 'Estrela'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCAO_CATEGORIA, default='')
    descricao= models.TextField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_publicada = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.nome