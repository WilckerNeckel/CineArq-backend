from django.urls import path
from .views import handle_form
urlpatterns = [
    path('api/formulario/handle_form/', handle_form.as_view(), name='handle_form'),

]
