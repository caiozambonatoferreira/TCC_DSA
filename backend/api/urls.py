from django.urls import path
from .views import get_articles

urlpatterns = [
    path('articles/', get_articles, name='get_articles'),
]