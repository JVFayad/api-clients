from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from clients import views

urlpatterns = [
    path('client/', views.ClientList.as_view()),
    path('client/<int:pk>/', views.ClientDetail.as_view()),
    path('client/<int:pk>/product-list', views.ClientProductList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)