from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view()),
    path('verify-email/', views.VerifyEmail.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('request-reset-email/', views.RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(),
         name='password-reset-confirm'),
    path('password-reset-complete/', views.SetNewPasswordAPIView.as_view()),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
