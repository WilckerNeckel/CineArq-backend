import io
from django.http import FileResponse
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
from .models import Formularios


class handle_form(APIView):
    
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            nome = data.get('Nome')
            email = data.get('Email')
            cpf = data.get('CPF')
            telefone = data.get('Telefone')
            codigo = data.get('Codigo')
            dados_inseridos = Formularios(nome=nome, email=email, cpf=cpf, telefone=telefone, codigo=codigo)
            dados_inseridos.save()
            return Response("Response: Dados enviados com sucesso", status=status.HTTP_200_OK)
        except Exception as e:
            print("erro: ", e)
            return Response(data={f'error': '{e}'}, status=status.HTTP_400_BAD_REQUEST)


