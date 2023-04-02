from django.db import models
from django.urls import reverse

class RoomModel(models.Model):
    
    guest = models.CharField("Nom complet", max_length=50, null=True)
    date_start = models.DateField("Date arrivée", auto_now=False, auto_now_add=False, null=True)
    date_end = models.DateField("Date sortie", auto_now=False, auto_now_add=False, null=True)
    nb_child = models.IntegerField("Nombre d'enfants", null=True)
    nb_adult = models.IntegerField("Nombre d'adultes", null=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chambre"
        verbose_name_plural = "Chambres"

    def __str__(self):
        return self.guest

    def get_absolute_url(self):
        return reverse("RoomModel_detail", kwargs={"pk": self.pk})


class RoomImageModel(models.Model):
    
    room = models.ForeignKey("room.RoomModel", on_delete=models.CASCADE, null=True)
    photos = models.ImageField(upload_to='rooms_photos/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Image de la chambre"
        verbose_name_plural = "Images des chambres"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("RoomImageModel_detail", kwargs={"pk": self.pk})
