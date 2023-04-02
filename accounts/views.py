from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from accounts.models import Profile, Contact
from accounts.forms import LoginForm, RegisterForm, UpdateProfileForm
from django.contrib.auth import  authenticate, login

  
    
def login_user(request): 
    context = {}
    if request.method == 'POST':
        error = 'Email ou mot de passe incorrect.' 
        form = LoginForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            account = User.objects.filter(email=email)
            
            context = {'error': error}
            
            if len(account):
                user = authenticate(username=account[0], password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'registration/login.html', context)
            else:
                return render(request, 'registration/login.html', context)
    else:
        form = LoginForm() 
    return render(request, 'registration/login.html', locals())

def create_account(request):   
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            name = request.POST['name'] 
            email = request.POST['email']
            password = request.POST['password']
             
            username = name.lower()
            username = username.replace(' ', '.')
            user_first_last_names = name.split(' ')
            
            if user_already_exist(email): 
                return render(request, 'registration/user_exist.html')
            
            else: 
                user = User.objects.create_user(
                    username=username, 
                    email=email, 
                    password=password,
                    first_name=user_first_last_names[0],
                    last_name=user_first_last_names[1],
                ) 
                
                authenticated_user = authenticate(
                    username=username, 
                    password=password,
                ) 
                
                if authenticated_user: login(request, authenticated_user)
             
                return redirect('accounts:update-profile')
           
        else:
                return render(request, 'registration/register.html', locals())
    else:
        form = RegisterForm() 
    return render(request, 'registration/register.html', locals())
 
def update_profile(request): 
    if request.method == 'POST': 
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid:  
            phone = request.POST['phone']
            gender = request.POST['gender'] 
            address = request.POST['address']
            bio = request.POST['bio']
            photo = request.FILES['photo']

            profile = Profile(
                user=request.user,
                phone=phone, 
                gender=gender,
                address=address,
                bio=bio,
                photo=photo
            )
            profile.save()
            
            return redirect('home')
        else: 
            form = UpdateProfileForm()
    else: 
        form = UpdateProfileForm()
    return render(request, 'registration/user_profile.html', locals())
 
def user_already_exist(email): 
    user = User.objects.filter(email=email)
    if user : 
        return True 
    else : 
        return False

def newsletter_suscription(request): 
    if request.method == 'POST': 
        user_email = request.POST['user_email']
        
        from accounts.models import NewsletterModel 
        newsletter = NewsletterModel(email=user_email)
        newsletter.save() 
        
        return render(request, 'registration/newsletter_done.html')
        
def profile(request): 
    user = request.user 
    if user: 
        profile = Profile.objects.get(user=user)
        return render(request, 'registration/profile.html', {'profile': profile}) 
    else: 
        return render(request, 'registration/user_profile.html')



class AccountsCreateView(CreateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('main:accounts-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = self.request.user
        context['accounts'] = accounts
        context["accounts_create"] = True
        context['accounts_app_create'] = 'Ajouter un novelle utilisateur'
        return context


class AccountsListView(ListView):

    model = Profile
    context_object_name = 'accounts_list'
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = self.request.user
        context['accounts'] = accounts
        context['accounts_list'] = Profile.objects.all()
        context['accounts_app_list'] = 'Liste de tous les utilisateurs'
        return context


class AccountsDeleteView(DeleteView):
    model = Profile
    context_object_name = 'accounts_delete'
    success_url = reverse_lazy('accounts:accounts-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = self.request.user
        context['accounts'] = accounts
        context['accounts_app_delete'] = "Supprimer l'utilisateur"
        return context


class AccountsUpdateView(UpdateView):
    model = Profile
    fields = '__all__'
    context_object_name = 'accounts_update'
    success_url = reverse_lazy('accounts:accounts-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = self.request.user
        context['accounts'] = accounts
        context['accounts_app_update'] = "Mettre à jour les données de l'utilisateur"
        return context


class AccountsDetailView(DetailView):
    model = Profile
    context_object_name = 'accounts_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = self.request.user
        context['accounts'] = accounts
        context['now'] = timezone.now()
        context['accounts_app_details'] = "Détails de l'utilisateur"
        return context


class MessageContactCreate(CreateView): 
    model = Contact
    context_object_name = 'message_contact'
    fields = '__all__'
    success_url = reverse_lazy('accounts:message-contact-sent')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = self.request.user 
        context['now'] = timezone.now()
        context['accounts'] = accounts
        context['contact_app_details'] = "Détails de l'utilisateur"
        return context