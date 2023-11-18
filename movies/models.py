from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    count = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title}"