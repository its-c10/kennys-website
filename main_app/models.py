from django.db import models
import datetime


# Create your models here.
class GalleryImage(models.Model):

    STAGE_1_DETAIL = "Stage 1"
    STAGE_2_DETAIL = "Stage 2"
    INTERIOR_DETAIL = "Interior Detail"
    SNOW_FOAMED = "Snow Foamed Detail"
    OTHER = "Other"

    car_name = models.CharField(max_length=255)
    DETAIL_TYPE_CHOICES = [
        (STAGE_1_DETAIL, STAGE_1_DETAIL),
        (STAGE_2_DETAIL, STAGE_2_DETAIL),
        (INTERIOR_DETAIL, INTERIOR_DETAIL),
        (SNOW_FOAMED, SNOW_FOAMED),
        (OTHER, OTHER),
    ]
    detail_type = models.CharField(
        max_length=18,
        choices=DETAIL_TYPE_CHOICES,
        default=OTHER,
    )

    date_added = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to="gallery_cars")
