from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.create_customer, name='customer_create'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('<int:pk>/update/', views.update_customer, name='customer_update'),
    path('<int:pk>/delete/', views.delete_customer, name='customer_delete'),
]
