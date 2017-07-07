from django.db import models

from events.models import Event

# Create your models here.

class NewEntry(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    event = models.ForeignKey(Event)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
