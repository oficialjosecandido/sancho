from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    lead = models.CharField(max_length=200, blank=True, null=True)
    image_src = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"