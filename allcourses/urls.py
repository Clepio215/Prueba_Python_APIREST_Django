from . import views
from django.urls import path


urlpatterns = [
    path('', views.courses),
    path('<codigo>/', views.ConsultDatos),
]