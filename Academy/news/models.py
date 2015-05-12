from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField( max_length=130)


class NewsComment(models.Model):
    date = models.DateField(auto_now_add=True)
    reviewer = models.ForeignKey(User,related_name='reviewer')
    content = models.TextField()

