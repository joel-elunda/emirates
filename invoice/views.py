from datetime import timezone
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.views.generic.list import ListView 
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView


from invoice.models import InvoiceModel



class InvoiceCreateView(CreateView):
    model = InvoiceModel
    fields = '__all__'
    success_url = reverse_lazy('main:room-create')
    template_view = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['user'] = self.request.user
        context["invoice_create"] = True
        context['invoice_app_create'] = 'Ajouter une nouvelle facture'
        return context


class InvoiceListView(ListView):
    template_view = 'list.html'
    model = InvoiceModel
    context_object_name = 'invoice_list'
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice = InvoiceModel.objects.all()
        context['invoice'] = invoice
        context['user'] = self.request.user
        context['invoice_list'] = InvoiceModel.objects.all()
        context['invoice_app_list'] = 'Liste de toutes les factures'
        return context


class InvoiceDeleteView(DeleteView):
    model = InvoiceModel
    context_object_name = 'invoice_delete'
    success_url = reverse_lazy('room:room-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['invoice_app_delete'] = "Supprimer la facture"
        return context


class InvoiceUpdateView(UpdateView):
    model = InvoiceModel
    fields = '__all__'
    context_object_name = 'invoice_update'
    success_url = reverse_lazy('room:room-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['invoice_app_update'] = "Mettre à jour les données de la facture"
        return context


class InvoiceDetailView(DetailView):
    model = InvoiceModel
    context_object_name = 'invoice_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.request.user
        context['room'] = room
        context['user'] = self.request.user
        context['now'] = timezone.now()
        context['invoice_app_details'] = "Détails de la facture"
        return context

 