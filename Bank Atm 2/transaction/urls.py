from django.urls import path
from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='transaction_list'),
    path('create/', views.TransactionCreateView.as_view(),
         name='transaction_create'),
    path('<int:pk>/', views.TransactionDetailView.as_view(),
         name='transaction_detail'),
    path('<int:pk>/update/', views.TransactionUpdateView.as_view(),
         name='transaction_update'),
    path('<int:pk>/delete/', views.TransactionDeleteView.as_view(),
         name='transaction_delete'),
]
