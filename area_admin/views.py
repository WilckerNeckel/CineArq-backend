from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import EnableForm
from django.contrib.auth.models import User

class enable_form(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def check_permissions(self, request):
        if request.method == 'GET':
            self.permission_classes = []
            self.authentication_classes = []
        return super().check_permissions(request)

    def get(self, request):
        try:
            is_enabled = EnableForm.objects.first().is_enabled
            print(is_enabled)
            return Response({"ResponseGET": str(is_enabled).lower()}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({f'GETerror': '{e}'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        try:
            
            form = EnableForm.objects.last()
            if form is None:
                return Response("No EnableForm objects in database", status=status.HTTP_400_BAD_REQUEST)
            
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            
            form.is_enabled = not form.is_enabled
            form.last_modified_user_id = user
            
            form.save()
            
            return Response({"ResponsePUT": str(form).lower()}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({f'PUTerror': '{e}'}, status=status.HTTP_400_BAD_REQUEST)

