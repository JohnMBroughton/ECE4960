from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.client_dashboard, name='client_dashboard'),
]
