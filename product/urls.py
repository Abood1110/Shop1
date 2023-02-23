from django.urls import path
from .views import HomeView ,ProductDetailView


app_name='product'

urlpatterns = [
    path('',HomeView.as_view()),
    path('product/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),

]