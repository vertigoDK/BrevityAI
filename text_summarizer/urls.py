from django.urls import path
from . import views


urlpatterns = [
    path('text_summarizer/', views.text_summarizer, name='text-summarizer'),
]
