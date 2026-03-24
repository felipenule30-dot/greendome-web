from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('age-gate/', views.age_gate, name='age_gate'),
    path('age-gate/confirm/', views.age_gate_confirm, name='age_gate_confirm'),
    path('acceso-denegado/', views.access_denied, name='access_denied'),
    path('api/register/', views.register_member, name='register_member'),
]
