from django.urls import path
from . import views

app_name = 'atm'

urlpatterns = [
    path('', views.atm_list, name='atm_list'),
    path('<int:pk>/', views.atm_detail, name='atm_detail'),
    path('create/', views.atm_create, name='atm_create'),
    path('<int:pk>/update/', views.atm_update, name='atm_update'),
    path('<int:pk>/delete/', views.atm_delete, name='atm_delete'),
]
