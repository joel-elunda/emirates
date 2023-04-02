from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class InvoiceModel(models.Model):
    client = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    plate = models.ForeignKey("plate.PlateModel",  on_delete=models.CASCADE, null=True)
    room = models.ForeignKey("room.RoomModel", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = "La Facture"
        verbose_name_plural = "Les Factures"

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse("InvoiceModel_detail", kwargs={"pk": self.pk})
