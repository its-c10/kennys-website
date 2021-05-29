from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "main_app"
urlpatterns = [
    path("", views.index, name="home-page"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery?view_type=all", views.gallery, name="gallery_all"),
    path("gallery?view_type=stage_1", views.gallery, name="gallery_s1"),
    path("gallery?view_type=stage_2", views.gallery, name="gallery_s2"),
    path("gallery?view_type=snow_foamed", views.gallery, name="gallery_sf"),
    path("gallery?view_type=interior_detail", views.gallery, name="gallery_id"),
    path("gallery?view_type=other", views.gallery, name="gallery_other"),
    path("services/", views.services, name="services"),
]
