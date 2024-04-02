from django.db import models
from django.contrib.auth.models import User
import os


def user_directory_path(instance, filename):
    # Construir o caminho para o diretório de upload baseado no ID do usuário
    user_id = instance.user.id
    return f'uploads/xls/user_{user_id}/{filename}'

class XlsFile(models.Model):
    
    file_name = models.CharField(max_length=100)
    file_size = models.IntegerField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Essa linha indica onde o arquivo deve ser armazenado no sistema de arquivos do servidor, e no banco de dados vai ser armazenado somente o caminho para o arquivo
    file_path = models.FileField(upload_to=user_directory_path)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.file_name
