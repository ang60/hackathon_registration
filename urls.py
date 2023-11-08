
# registration/urls.py
from django.urls import path
from views import*

urlpatterns = [
    path('register/',register_participant, name='register_participant'),
    path('registration_success/',registration_success, name='registration_success'),
]
