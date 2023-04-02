
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class UserAddress(models.Model):
    country = models.CharField(
        'Pays', max_length=60, default="République Démocratique du Congo", blank=True, null=True)
    province = models.CharField(
        'Province', max_length=60, default="Haut-Katanga", blank=True, null=True)
    city = models.CharField('Ville', max_length=60,
                            default="Lubumbashi", blank=True, null=True)
    commune = models.CharField(
        'Commune', max_length=60, default="Lubumbashi", blank=True, null=True)
    quarter = models.CharField(
        'Quartier', max_length=60, blank=True, null=True)
    avenue = models.CharField('Avenue', max_length=60, blank=True, null=True)
    number = models.CharField('Numéro', max_length=5, blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True,
                            help_text='Valeur unique pour l\'URL de la page du produit, créée à partir du nom.', blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = 'Adresse utilisateur'
        verbose_name_plural = 'Adresses utilisateurs'

    def __str__(self):
        return '%s %s %s' % (self.country, self.province, self.city, )

    def get_absolute_url(self):
        return reverse("UserAddress_detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    GENDER = (
        ('F', 'Féminin'),
        ('M', 'Masculin'),
    )

    user = models.OneToOneField(
        User, verbose_name='Utilisateur', on_delete=models.CASCADE, blank=True, null=True, )
    # enterprise = models.ForeignKey(Enterprise, verbose_name='Employé à ', on_delete=models.CASCADE, blank=True, null=True,)
    # enterprise = main.models.Enterprise()
    gender = models.CharField('Genre',  choices=GENDER,
                              max_length=1, blank=True, null=True,)
    phone = models.CharField('Numéro de téléphone',
                             max_length=20, blank=True, null=True,)
    bio = models.TextField(blank=True, null=True, max_length=100)
    photo = models.ImageField('Image', null=True, upload_to='users-photos/',
                              height_field=None, width_field=None, max_length=None) 
    address = models.CharField('Adresse', max_length=50, null=True)
    slug = models.SlugField(max_length=150, unique=True,
                            help_text='Unique value for product page URL, created from name.', blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s (%s)' % (self.user, self.address, self.phone)
        # return '%s %s (%s)' % (self.user.first_name, self.user.last_name, self.user.groups.all()[0].name)

    class Meta:
        managed = True
        verbose_name = 'Profile d\'utilisateur'
        verbose_name_plural = 'Profile des utilisateurs'

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class CommentModel(models.Model):
    user = models.ForeignKey(
        "accounts.Profile", on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("CommentModel_detail", kwargs={"pk": self.pk})


class Contact(models.Model):
    
    name = models.CharField('Nom du complet', max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField('Téléphone', null=True, max_length=50)
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Message reçu"
        verbose_name_plural = "Messages reçus"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})

class NewsletterModel(models.Model):
    
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Souscription à la Newsletter'
        verbose_name_plural = 'Souscriptions à la Newsletter'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("NewsletterModel_detail", kwargs={"pk": self.pk})

