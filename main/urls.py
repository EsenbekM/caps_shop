from django.urls import path
from . import views

urlpatterns = [
    path('caps/', views.CapListAPIView.as_view()),
    path('caps/<int:id>/', views.CapDetailAPIView.as_view()),
    path('brand/', views.BrandListAPIView.as_view()),
    path('brand/<int:pk>/', views.BrandCapListAPIView.as_view()),
] 