from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('', include('login.urls')),
    path('atm', include('atm.urls')),
    path('transaction', include('transaction.urls')),
]
