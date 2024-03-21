from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Stores a single category.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    fa_string = models.CharField(max_length=100)
    colour = models.CharField(max_length=7)

    