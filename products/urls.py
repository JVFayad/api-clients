from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)