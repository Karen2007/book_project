from django.db import models

# Create your models here.
class Review(models.Model):
    photo = models.ImageField(upload_to='books/photos')
    title = models.CharField(max_length=80)
    description = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title