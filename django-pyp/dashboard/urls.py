from django.urls import path
from dashboard import views
from django.contrib import admin

urlpatterns = [
    path('', views.client_dashboard, name='client_dashboard'),
]

admin.site.site_header = 'Pick Your Park'
