from django.db import models
from geoposition.fields import GeopositionField
from django.utils import timezone

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    position = GeopositionField(blank=True)

    class Meta:
        verbose_name_plural = 'points of interest'