from .api import (
    PersonListAPIView,
    CreatePersonAPIView,
    UpdatePersonAPIView,
    DeletePersonAPIView,
)
from django.urls import path
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiosk.settings")

app_name = 'profiling'
urlpatterns = [
    path(r'persons/', PersonListAPIView.as_view(), name='api-person-create'),
    path(r'persons/create/', CreatePersonAPIView.as_view(), name='api-person-create'),
    path(r'persons/<int:id>/update/', UpdatePersonAPIView.as_view(), name='api-person-update'),
    path(r'persons/<int:id>/delete/', DeletePersonAPIView.as_view(), name='api-person-delete'),
]