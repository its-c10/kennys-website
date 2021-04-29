from django.db import models
import datetime

# Create your models here.
class GalleryImage(models.Model):
    car_name = models.CharField(max_length=255)
    detail_type = models.CharField(max_length=255)
    date_added = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to="gallery_cars")
