from django.db import models

class Outlet(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    operating_hours = models.CharField(max_length=255)
    waze_link = models.URLField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.name
