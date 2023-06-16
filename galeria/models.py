from django.db import models

from datetime import datetime

class Fotografia(models.Model):
    OPCAO_CATEGORIA=[
        ('NEBULOSA', 'Nebulosa'),
        ('GALÁXIA', 'Galáxia'),
        ('ESTRELA', 'Estrela'),
        ('PALNETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCAO_CATEGORIA, default='')
    descricao= models.TextField(max_length=100, null=False, blank=False)
    foto = models.FileField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_publicada = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return f'Fotografia [nome={self.nome}]'