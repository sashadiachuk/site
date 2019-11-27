from django.db import models
class Teacher_dotsent (models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(max_length=11500, null=True, blank=True)
    image = models.ImageField(upload_to="personal/media/img/", default=True)
    def __str__(self):
        return self.name
class Teacher_prof(models.Model):
        name = models.CharField(max_length=64, blank=True, null=True, default=None)
        description = models.TextField(max_length=11500, null=True, blank=True)
        image = models.ImageField(upload_to="personal/media/img/", default=True)

        def __str__(self):
            return self.name
class Teacher_st_vikl(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(max_length=11500, null=True, blank=True)
    image = models.ImageField(upload_to="personal/media/img/", default=True)

    def __str__(self):
        return self.name











