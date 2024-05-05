from django.urls import path, include
from .views import WorkSheetView, gerenerate_worksheet



urlpatterns = [

    path('api/worksheet/transform_worksheet/', WorkSheetView.as_view(), name='worksheet'),
    path('api/worksheet/generate_worksheet/', gerenerate_worksheet.as_view(), name='generate_worksheet'),
    

]
