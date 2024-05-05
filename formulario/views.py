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
            print(dados_inseridos)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(data={'error': 'Erro ao enviar formulário'}, status=status.HTTP_400_BAD_REQUEST)

