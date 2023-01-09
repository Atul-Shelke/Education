from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('nav',v.home),
    path('login',v.login)
]
