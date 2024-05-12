from django.urls import path
from .views import enable_form
urlpatterns = [
    path('api/admin_area/enable_link/', enable_form.as_view(), name='enable_form'),

]
