from django.db import models

class abitura (models.Model):
    email = models.EmailField()
    text = models.TextField(max_length=122)
    #name = models.CharField(max_length=122)
# Create your models here.

