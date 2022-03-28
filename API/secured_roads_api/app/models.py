from django.db import models

class x(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

