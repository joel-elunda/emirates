from django.contrib import admin
from accounts.models import *


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'id', 'slug', 'user']
    prepopulated_fields = {'slug': ('user', 'phone'), }


class UserAddressAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'id', 'slug', 'country', 'city', 'number']
    prepopulated_fields = {'slug': ('country', 'number'), }


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsletterModel)
class NewsletterAdmin(admin.ModelAdmin): 
    pass

 
admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
