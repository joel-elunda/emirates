from datetime import timezone
from room.forms import RoomModelForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.views.generic.list import ListView 
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView

from room.models import RoomModel



def create_room_order(request): 
    if request.method == 'POST' : 
        form = RoomModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            guest =  guest.request.POST['guest']
            date_start =  date_start.request.POST['date_start']
            date_end =  date_end.request.POST['date_end']
            nb_child =  nb_child.request.POST['nb_child']
            nb_adult =  nb_adult.request.POST['nb_adult']
            
            room = RoomModel(
                guest = guest,
                date_start = date_start,
                date_end = date_end,
                nb_child = nb_child,
                nb_adult = nb_adult,
            )
            
            room.save
            


class RoomCreateView(CreateView):
    model = RoomModel
    fields = '__all__'
    success_url = reverse_lazy('main:room-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.request.user
        context['room'] = room
        context['user'] = self.request.user
        context["room_create"] = True
        context['room_app_create'] = 'Ajouter une nouvelle chambre'
        return context


class RoomListView(ListView):

    model = RoomModel
    context_object_name = 'room_list'
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.request.user
        context['room'] = room
        context['user'] = self.request.user
        context['room_list'] = RoomModel.objects.all()
        context['room_app_list'] = 'Liste de toutes les chambres'
        return context


class RoomDeleteView(DeleteView):
    model = RoomModel
    context_object_name = 'room_delete'
    success_url = reverse_lazy('room:room-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.request.user
        context['room'] = room
        context['user'] = self.request.user
        context['room_app_delete'] = "Supprimer la chambre"
        return context


class RoomUpdateView(UpdateView):
    model = RoomModel
    fields = '__all__'
    context_object_name = 'room_update'
    success_url = reverse_lazy('room:room-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.request.user
        context['room'] = room
        context['user'] = self.request.user
        context['room_app_update'] = "Mettre à jour les données de la chambre à louer"
        return context


class RoomDetailView(DetailView):
    model = RoomModel
    context_object_name = 'room_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.request.user
        context['room'] = room
        context['user'] = self.request.user
        context['now'] = timezone.now()
        context['room_app_details'] = "Détails de la chambre à louer"
        return context

 