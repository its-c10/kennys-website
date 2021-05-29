from django.contrib import admin

from .models import GalleryImage
from .models import Service

# Register your models here.
admin.site.register(GalleryImage)
admin.site.register(Service)