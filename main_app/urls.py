from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "main_app"
urlpatterns = [
    path("", views.index, name="home-page"),
]