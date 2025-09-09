from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    season = models.CharField(max_length=9)
    exlusive = models.BooleanField(default=False)

    def __str__(self):
        return self.name
