from django.urls import path, include
from rest_framework import routers
from .views import IsValidTokenView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/isvalid/', IsValidTokenView.as_view(), name='isvalid'),

]

"""
router = routers.DefaultRouter()
router.register('auth', TokenView, basename='auth')

urlpatterns = [
    path('', include(router.urls)),

]
"""