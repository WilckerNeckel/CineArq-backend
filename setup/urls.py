from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('worksheet.urls')),
    path('', include('formulario.urls')),
    path('', include('area_admin.urls')),
]
