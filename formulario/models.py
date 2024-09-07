from django.db import models

class Formularios(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    codigo = models.CharField(max_length=10)

    class Meta:
        db_table = 'formularios'

    def __str__(self):
        return self.nome