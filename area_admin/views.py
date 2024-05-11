from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import EnableForm

class enable_form(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    
    def check_permissions(self, request):
        if request.method == 'GET':
            self.permission_classes = []
            self.authentication_classes = []
        return super().check_permissions(request)

    def get(self, request):
        is_enabled = EnableForm.objects.last().is_enabled
        return Response({"is_enabled": is_enabled}, status=status.HTTP_200_OK)
        

    def put(self, request):
        user_id = request.user.id
        form = EnableForm.objects.last()
        
        if form is None:
            return Response("No EnableForm objects in database", status=status.HTTP_400_BAD_REQUEST)
        
        form.is_enabled = not form.is_enabled
        form.last_modified_user_id = user_id
        form.save()
        return Response(f"Response: Formulario: {form.is_enabled}", status=status.HTTP_200_OK)

