from .models import Usuario
from rest_framework import serializers
from rest_framework.authtoken import views 


class SmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'message', 'sender', 'recipient']
