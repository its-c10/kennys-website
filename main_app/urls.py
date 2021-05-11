from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "main_app"
urlpatterns = [
    path("", views.index, name="home-page"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/<str:view_type>/", views.gallery, name="gallery_all"),
    path("gallery/<str:view_type>/", views.gallery, name="gallery_s1"),
    path("gallery/<str:view_type>/", views.gallery, name="gallery_s2"),
    path("gallery/<str:view_type>/", views.gallery, name="gallery_sf"),
    path("gallery/<str:view_type>/", views.gallery, name="gallery_id"),
    path("gallery/<str:view_type>/", views.gallery, name="gallery_other"),
]
