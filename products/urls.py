from django.urls import path
from django.views.decorators.cache import cache_page
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('product/', cache_page(
        settings.CACHE_TIME)(views.ProductList.as_view())),
        
    path('product/<int:pk>/', cache_page(
        settings.CACHE_TIME)(views.ProductDetail.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)