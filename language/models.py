from django.db import models


class Language(models.Model):
    slug = models.SlugField(max_length=50, unique=True, default='language')
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    usage = models.CharField(max_length=100)

    def __str__(self):
        return self.name
