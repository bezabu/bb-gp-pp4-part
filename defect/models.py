from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Stores a single category.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    fa_string = models.SlugField(max_length=100)
    colour = models.CharField(max_length=7)

STATUS = ((0, "Open"), (1, "Resolved"), (2, "Sticky"))

class Defect(models.Model):
    """
    Stores a single defect, related to :model:'Category' and :model:'auth.User'
    """
    defect_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="defects")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reporter")
    body = models.TextField()
    image_url = models.SlugField()
    reported_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    reoccurance = models.IntegerField()
