from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.contrib.auth.models import User 
from django.contrib.auth import  authenticate, login
from accounts.models import Profile
from accounts.forms import CreateProfileForm

from django.views.generic.list import ListView 
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView

REGISTRATION_LOGIN = 'registration/login.html'
REGISTRATION_PROFILE = 'registration/profile.html'

def login_user(request): 
    context = {}
    error = {'login_incorrect': 'Email ou mot de passe incorrect.'}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            account = User.objects.filter(email=email)
            if len(account):
                user = authenticate(username=account[0], password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, REGISTRATION_LOGIN, error)
            else:
                return render(request, REGISTRATION_LOGIN, error)
    else:
        form = LoginForm() 
    return render(request, REGISTRATION_LOGIN, context)



def get_current_profile(request):
    if request.user.is_authenticated:
        profile = {'profile' : Profile.objects.filter(user=request.user)} 
        return render(request, REGISTRATION_PROFILE, profile) 
 
 

def get_user_profile(request, pk):  
    user_profile, context = Profile.objects.filter(pk=pk), {}
    if user_profile:
        context = { 'user_profile': user_profile  }
    else:
        context = { 'no_profile_found' : "Cette utilisateur n'a pas encore de profile" }
    return render(request, REGISTRATION_PROFILE, context)



def create_or_update_profile(request, pk): 
    form = CreateProfileForm(request.POST)
    
    if form.is_valid:
        user = request.user
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        phone = request.POST['phone']
        bio = request.POST['bio']
        photo = request.FILES['photo']
        address = request.POST['address'] 
        
        profile = Profile(
            user=user, 
            user__first_name = first_name,
            user__last_name = last_name,
            gender=gender, 
            phone=phone, 
            bio=bio, 
            photo=photo, 
            address=address
        )
        
        profile.save() 
        
        return redirect('profile')
    else:
        form = CreateProfileForm()
    
    return render(request, 'create.html', locals())
 

class AccountsListView(ListView):
    model = Profile
    template_name = 'list.html'
    context_object_name = 'account_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts_list_title'] = \
            'Liste de tout le personnel'
        context['accounts_list_description'] = \
            'Description élargie de tout le personnel en fonction.'
        return context
    
    
class AccountsDetailView(DetailView):
    model = Profile
    template_name = 'read.html'
    context_object_name = 'account_details'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_details_title'] = \
            'Détails du personnel'
        context['account_details_description'] = \
            'Informations relatives aux personnel'
        return context
    
class AccountsDeleteView(DeleteView):
    model = Profile
    template_name = 'delete.html'
    context_object_name = 'accounts_delete'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account_delete_title"] = \
            "Suppression du personnel"
        context["account_delete_description"] = \
            "La suppression pourrait entrainer l'effacement de la trace de cette opération"
        return context