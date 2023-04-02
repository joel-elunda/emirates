from django.db import models 
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone

class PlateModel(models.Model):
    client = models.CharField( max_length=50, null=True)
    name = models.CharField("Nom du plat", max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(
        'Date de création', default=timezone.now)
    updated_at = models.DateTimeField(
        'Date de modification', auto_now=True)
    
    class Meta:
        verbose_name = "Plat et Restauration"
        verbose_name_plural = "Plats et Restaurations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PlateModel_detail", kwargs={"pk": self.pk})
 