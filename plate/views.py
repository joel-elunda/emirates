from django.shortcuts import render

from django.views.generic.list import ListView 
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView

from plate.models import PlateModel 
from plate.forms import PlateModelForm



class PlateCreateView(CreateView): 
    model = PlateModel
    template_view = 'create.html'
    success_url = reverse_lazy('plate:user-details')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plate"] = PlateModel
        context['user'] = self.request.user
        context['plate_app_create'] = 'Ajouter un nouveau plat'
        return context
      


class PlateListView(ListView): 
    model = PlateModel
    template_view = 'list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plate"] = PlateModel.objects.all()
        context['user'] = self.request.user
        context['plate_app_list'] = 'Liste de tous les plats'
        return context
      


class PlateDeleteView(DeleteView): 
    model = PlateModel
    template_view = 'delete.html'
    success_url = reverse_lazy('plate:list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['user'] = self.request.user
        context['plate_app_delete'] = "Supprimer le plat"
        return context
      


class PlateUpdateView(UpdateView): 
    model = PlateModel
    template_view = 'update.html'
    success_url = reverse_lazy('plate:list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['user'] = self.request.user
        context['plate_app_update'] = "Mettre à jour les données du plat"
        return context
      


class PlateDetailView(DeleteView): 
    model = PlateModel
    template_view = 'details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['user'] = self.request.user
        context['plate_app_details'] = "Détails du plat"
        return context
      






