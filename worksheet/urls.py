from django.urls import path, include
from .views import WorkSheetView 



urlpatterns = [

    path('api/worksheet/', WorkSheetView.as_view(), name='worksheet'),

]
