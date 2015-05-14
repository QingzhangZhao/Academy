from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField( max_length=130)
    content = models.TextField()
    images = models.ImageField(blank=True,upload_to='./static/images/')
   # view = models.IntegerField()
   # cNum = models.IntegerField()


#class NewsComment(models.Model):
#    news = models.ForeignKey(News,related_name='comment')
#    date = models.DateField(auto_now_add=True)
#    reviewer = models.ForeignKey(User,related_name='reviewer')
#    content = models.CharField(max_length=150)
#    image = models.ImageField(blank=True,upload_to='./static/images/')


#:

