from django.urls import path
from .views import TranscripcionView

urlpatterns = [
    path('transcribe/', TranscripcionView.as_view(), name='transcribe'),
]
