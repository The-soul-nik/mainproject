from django.db import models

# Create your models here.
class Minimalism(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb  = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title



class Abstraction(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb  = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title


class Landscapes(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb  = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title
