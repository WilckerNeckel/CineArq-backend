from django.urls import path, include
from rest_framework import routers
from .views import IsValidTokenView, get_authenticated_username, login_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/isvalid/', IsValidTokenView.as_view(), name='isvalid'),
    #path('api/files/xls/'),
    path('api/auth/login/', login_view, name='login'),
    path('api/auth/logout/', logout_view, name='logout'),
    path('api/auth/get_username', get_authenticated_username, name='get_username'),

]

"""
router = routers.DefaultRouter()
router.register('auth', TokenView, basename='auth')

urlpatterns = [
    path('', include(router.urls)),

]
"""