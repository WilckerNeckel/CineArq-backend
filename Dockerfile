# Use uma imagem base Python
FROM python:3.10-slim

# Instalar as dependências do PostgreSQL e compilador C
RUN apt-get update && apt-get install -y libpq-dev gcc

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o container
COPY requirements.txt /app/

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do projeto para o container
COPY . /app/

# Exponha a porta que será utilizada pelo Django (8000 por padrão)
EXPOSE 8000

# Comando para rodar o servidor Django dentro do container

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
