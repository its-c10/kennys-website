from django.db import models
import datetime


# Create your models here.
class GalleryImage(models.Model):

    STAGE_1_DETAIL = "stage_1"
    STAGE_2_DETAIL = "stage_2"
    INTERIOR_DETAIL = "interior_detail"
    SNOW_FOAMED = "snow_foamed"
    OTHER = "other"

    car_name = models.CharField(max_length=255)
    DETAIL_TYPE_CHOICES = [
        (STAGE_1_DETAIL, "Stage 1"),
        (STAGE_2_DETAIL, "Stage 2"),
        (INTERIOR_DETAIL, "Interior Detail"),
        (SNOW_FOAMED, "Snow Foamed"),
        (OTHER, "Other"),
    ]
    detail_type = models.CharField(
        max_length=18,
        choices=DETAIL_TYPE_CHOICES,
        default=OTHER,
    )

    date_added = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to="gallery_cars")

    def __str__(self) -> str:
        return self.car_name + " | " + self.detail_type


class Service(models.Model):

    service_type = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.service_type
