from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=200,unique=True)
    language=models.CharField(max_length=200)
    run_time=models.PositiveIntegerField()
    genre=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    actors=models.CharField(max_length=200)

    def __str__(self):
        return self.name

