from django.db import models
from django.urls import reverse
from hashid_field import HashidAutoField


# Create your models here.
class TimeStamps(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now_add=True, null=True, blank=True)
    class Meta:
        abstract = True

class StyleMusical(TimeStamps):
    reference_id = HashidAutoField(primary_key=True, unique=True)
    style = models.CharField(blank=True, max_length=150, null=True)
 
    def __str__(self):
        return self.style

    def get_absolute_url(self):
        return reverse("StyleMusical_detail", kwargs={"pk": self.pk})