from django.db import models

class Task(models.Model):
    vazifa_nomi = models.CharField(max_length=100)
    vazifa_tafsifi = models.TextField()
    status = models.BooleanField(default=False)


