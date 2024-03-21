from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Open"), (1, "Resolved"), (2, "Sticky"))

class Category(models.Model):
    """
    Stores a single category.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    fa_string = models.SlugField(max_length=100)
    colour = models.CharField(max_length=7)

    def __str__(self):
        return f"Category: {self.name}"


class Defect(models.Model):
    """
    Stores a single defect, related to :model:'Category' and :model:'auth.User'
    """
    defect_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="defects")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reporter")
    body = models.TextField()
    #image_url = models.SlugField()
    reported_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    reoccurance = models.IntegerField(default=0)
    updates_count = models.IntegerField(default=0)
    latest_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-reported_on"]

    def __str__(self):
        return f"Defect: {self.title} ({self.category})"
