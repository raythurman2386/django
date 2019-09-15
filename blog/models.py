from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField()
    pub_date = models.DateField()
    body = models.CharField()
    image = models.ImageField(upload_to=)
