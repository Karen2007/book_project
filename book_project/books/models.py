import datetime

from django.db import models

# Create your models here.
class Review(models.Model):
    photo = models.ImageField(upload_to='books/photos')
    title = models.CharField(max_length=80)
    description = models.TextField()
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment_text = models.TextField()
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
