"""emirates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from accounts.views import *
from . import views
from accounts.views import (
    AccountsCreateView,
    AccountsListView,
    AccountsDeleteView,
    AccountsUpdateView,
    AccountsDetailView,
    MessageContactCreate,
)
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [ 
                   path('login/', views.login_user, name='login'),
    path('unlock/', auth_views.LoginView.as_view(
        template_name="layouts/lock-screen.html"), name='unlock'),
    path('logout',  auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', login_required((AccountsDetailView.as_view(
        template_name='registration/user-profile.html'))), 
        name='profile'),
    path('user-list/', login_required((AccountsListView.as_view(template_name='user/list.html'))),
         name='user-list'),
    path('register/', views.create_account, name='register'),
    path('update/<int:pk>',
         login_required((AccountsUpdateView.as_view(template_name='update.html'))), name='update'),
    path('delete/<int:pk>',
         login_required((AccountsDeleteView.as_view(template_name='delete.html'))), name='delete'),
    path('details/<int:pk>',
        login_required((AccountsDetailView.as_view(
            template_name='details.html'))), 
            name='details'),
    # path('lock-screen', views.unlock, name='lock-screen'),

    path('change-password/', auth_views.PasswordChangeView.as_view(),
        name='change-password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), 
        name='password-reset'),
    
    path('lock-screen', TemplateView.as_view(
        template_name=''), 
        name='lock-screen'), 
    
    path('message-contact/', MessageContactCreate.as_view(
        template_name='contact.html'), name='message-contact'
    ),
    
    path('message-contact-sent/', 
        TemplateView.as_view(
        template_name='layouts/message_contact_sent.html'),
        name='message-contact-sent',),
    
    path('update-profile/', login_required(views.update_profile), 
        name='update-profile'),
    
    path('newsletter-suscription', views.newsletter_suscription, name='newsletter-suscription'),
    
    path('profile', views.profile, name='profile'),
]  