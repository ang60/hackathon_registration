
# registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_participant, name='register_participant'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
