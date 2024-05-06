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
from .models import XlsFile

class login_view(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(email=email).first()
        if user is not None:
            username = user.username
        else:
            return JsonResponse({'error': 'Usuário não encontrado.'}, status=400)
        
        autenticar = authenticate(request, username=username, password=password)
        print(user)
        
        
        if autenticar is not None:
            # O usuário foi autenticado com sucesso, então podemos logá-lo
            django_login(request, autenticar)
            return JsonResponse({'message': 'Login realizado com sucesso.'})
        else:
            return JsonResponse({'error': 'Usuário ou senha inválidos.'}, status=400)

class return_username(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        username = User.objects.filter(email=email).first().username
        return JsonResponse({'username': username})

        
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

class upload_xls_file(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    
    def post(self, request):
        
        uploaded_file = request.FILES['file']
        user_id = request.user.id
        file_instance = XlsFile.objects.create(
            file_path=uploaded_file,
            file_name=uploaded_file.name,
            file_size=uploaded_file.size,
            user_id=user_id
        )
        if upload_xls_file:
            return JsonResponse({'message': 'Arquivo enviado com sucesso!'})
        
        else:
            return JsonResponse({'error': 'Falha ao enviar o arquivo'}, status=400)
        

class IsValidTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Se chegou até aqui, o token é válido
        return JsonResponse({'message': 'Token válido.'})