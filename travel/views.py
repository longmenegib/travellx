from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .models import Registration_form, Ticket, Bus
from .forms import Reg, TicketForm, Signing
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate




def home(request):
    isloggin = True
    return render(request, 'travel/travellx_home.html', locals())

def agency(request):
    isloggin = True
    return render(request, 'travel/agency.html', locals())



def language(request):
    return render(request, 'travel/language.html', locals())

def register(request):
    isloggin = True
    form = Reg(request.POST or None)
    if form.is_valid():
        form.save()
        renvoi = True
        users = Registration_form.objects.all()
    return render(request, 'travel/register.html', locals())

@login_required(login_url='loging')
def ticket(request): 
    isloggin = True
    if request.method == 'POST': 
        form = TicketForm(request.POST or None)
        if form.is_valid(): 
            envoi = True
            TicketForm.user = request.user
            
            form.save()
            users = Ticket.objects.all()
            return redirect('transaction')
        else:
            envoi = False
    else:
        form = TicketForm()
    return render(request, 'travel/ticket.html', {'form': form})
@login_required(login_url='loging')
def transaction(request):
    isloggin = True
    user = request.user
    status = False
    for userpro in Ticket.objects.filter(user=user):
        if userpro.user == user.id:
            userpro = user
    return render(request, 'travel/transaction.html', locals())
    
def signingView(request):
    if request.user.is_authenticated:
        return redirect('ticket')
    else:
        if request.method == 'POST':
            form = Signing(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('ticket')
        else:
            form = signingView
    return render(request, 'travel/signup.html', {'form': form})   

def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
    return render(request, 'travel/login.html', context)

def log_out(request):
    logout(request)  
    return redirect('loging')