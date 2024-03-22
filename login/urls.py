from django.urls import path, include
from rest_framework import routers
from .views import IsValidTokenView, get_user_credentials, login_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth import views as auth_views



urlpatterns = [

    #minhas rotas
    path('api/auth/token/isvalid/', IsValidTokenView.as_view(), name='isvalid'),
    #path('api/files/xls/'),
    path('api/auth/login/', login_view.as_view(), name='login'),
    path('api/auth/logout/', logout_view.as_view(), name='logout'),
    path('api/auth/get_username/', get_user_credentials.as_view(), name='get_username'),
    
    #rotas do django
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    #rotas do simple jwt
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

"""
router = routers.DefaultRouter()
router.register('auth', TokenView, basename='auth')

urlpatterns = [
    path('', include(router.urls)),

]
"""