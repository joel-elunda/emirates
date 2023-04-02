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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from invoice.views import (
    InvoiceCreateView,
    InvoiceListView,
    InvoiceDeleteView,
    InvoiceUpdateView,
    InvoiceDetailView,
)

app_name = 'invoice'

urlpatterns = [ 
    path('create/', InvoiceCreateView.as_view(), name='create'),
    path('list/', InvoiceListView.as_view(), name='list'),
    path('delete/<int:pk>/', InvoiceDeleteView.as_view(), name="delete"),
    path('update/<int:pk>/', InvoiceUpdateView.as_view(), name='update'),
    path('details/<int:pk>/', InvoiceDetailView.as_view(), name='details'),
]  