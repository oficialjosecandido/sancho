from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teste, name='test'),
    path('link', views.get_news_details, name='link'),

    # frontend
    # path('news', views.get_news, name='news'),
]
