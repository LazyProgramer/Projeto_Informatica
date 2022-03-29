from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Alert(models.Model):
    source = models.CharField(max_length=100)
    #max length for title + description = tweet length
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=230) 
    level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
     )
    #TODO: check for a better way to store locations
    location = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
