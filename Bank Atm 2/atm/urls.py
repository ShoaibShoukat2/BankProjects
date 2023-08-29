from django.urls import path
from . import views

app_name = 'atm'

urlpatterns = [
    path('', views.AtmListView.as_view(), name='atm_list'),
    path('<int:pk>/', views.AtmDetailView.as_view(), name='atm_detail'),
    path('create/', views.AtmCreateView.as_view(), name='atm_create'),
    path('<int:pk>/update/', views.AtmUpdateView.as_view(), name='atm_update'),
    path('<int:pk>/delete/', views.AtmDeleteView.as_view(), name='atm_delete'),
]
