import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class login_view(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('email')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        
        
        if user is not None:
            # O usuário foi autenticado com sucesso, então podemos logá-lo
            django_login(request, user)
            return JsonResponse({'message': 'Login realizado com sucesso.'})
        else:
            return JsonResponse({'error': 'Usuário ou senha inválidos.'}, status=400)
    
class logout_view(APIView):
    def post(self, request):
        django_logout(request)
        return JsonResponse({'message': 'Logout realizado com sucesso.'})

class get_user_credentials(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        username = request.user.username
        return JsonResponse({'username': username})





"""def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('email')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        
        
        if user is not None:
            # O usuário foi autenticado com sucesso, então podemos logá-lo
            django_login(request, user)
            return JsonResponse({'message': 'Login realizado com sucesso.'})
        else:
            return JsonResponse({'error': 'Usuário ou senha inválidos.'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)"""
    
    
"""
def logout_view(request):
    
    if request.method == 'POST':
        django_logout(request)
        return JsonResponse({'message': 'Logout realizado com sucesso.'})
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)
    """
def SaveXls(request):
    pass


class IsValidTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Se chegou até aqui, o token é válido
        return Response({"isvalid": "true"})


'''from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, authentication
from .serializers import SmsSerializer
from .models import SmsInfo


class TwilioWebhookView(APIView):

    def post(self, request):
        # Validar os dados recebidos da Twilio
        try:
            message_body = request.data['Body']
            sender = request.data['From']
            recipient = request.data['To']
        except KeyError as chave_json:
            return Response({'detail': f'Campo obrigatório ausente: {chave_json}'}, status=status.HTTP_400_BAD_REQUEST)

        # Validar  os dados de acordo com as regras que coloquei no serializer, nesse caso nenhuma, o papel do serializer vai ser pegar os dados recebidos por http, e salvar no banco de dados com o serializer.save()
        serializer = SmsSerializer(data={
            'message': message_body,
            'sender': sender,
            'recipient': recipient
        })

        if serializer.is_valid():
            serializer.save()

            # Enviar uma resposta de confirmação para a Twilio
            response = MessagingResponse()
            response.message("Mensagem recebida com sucesso!")
            return Response(str(response))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SmsInfoListView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = SmsSerializer(SmsInfo.objects.all(), many=True)
        return Response(serializer.data)'''
        
        

