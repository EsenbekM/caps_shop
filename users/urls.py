from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('users/register/', views.RegistrationAPIView.as_view()),
    path('users/verify-email/', views.VerifyEmail.as_view()),
    path('users/login/', views.LoginAPIView.as_view()),
    path('users/request-reset-email/', views.RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('users/password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(),
         name='password-reset-confirm'),
    path('users/password-reset-complete/', views.SetNewPasswordAPIView.as_view()),


    path('users/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
