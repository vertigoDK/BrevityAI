from django.urls import path
from . import views


urlpatterns = [
    path('site-summarizer/', views.site_summarizer_view, name='site-summarizer')
]
