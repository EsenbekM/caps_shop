from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/caps/', views.CapListAPIView.as_view()),
    path('api/v1/caps/<int:id>/', views.CapDetailAPIView.as_view()),
    path('api/v1/brand/', views.BrandListAPIView.as_view()),
    path('api/v1/brand/<int:pk>/', views.BrandCapListAPIView.as_view()),
] 