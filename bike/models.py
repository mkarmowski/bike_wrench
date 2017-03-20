from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


BIKE_PARTS_TYPES = (
    ('frame', 'Frame'),
    ('fork', 'Fork'),
    ('damper', 'Damper'),  # TODO choices for bike parts
)


class Bike(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='bike')
    mileage = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bike:bike_details', args=[self.id])


class BikePart(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    type = models.CharField(choices=BIKE_PARTS_TYPES, max_length=100)
    mileage = models.DecimalField(max_digits=12, decimal_places=2)
    bike_mounted = models.ForeignKey(Bike, related_name='parts')
    mount_date = models.DateField()
    last_service_date = models.DateField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bike:part_details', args=[self.id])

