from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from clients import views

urlpatterns = [
    path('client/', views.ClientListCreate.as_view(), 
        name="create_list_clients"),

    path('client/<int:pk>/', views.ClientRetrieveUpdateDestroy.as_view(), 
        name="detail_update_delete_clients"),
        
    path('client/<int:pk>/product-list/', views.ClientProductList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)