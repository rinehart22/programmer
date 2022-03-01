from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
from . forms import *
def home(request):
    q = programmer.objects.all()
    return render(request,'home.html', {'q':q})


def create(request):  
    form = ProgrammerForm()
    if request.method == 'POST':  
        form = ProgrammerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
        return redirect('/')
    
    return render(request, 'create.html', {'form': form})

def update(request, id):  
    r = programmer.objects.get(pk=id)
    form = ProgrammerForm(instance=r)
    if request.method == 'POST':
        form = ProgrammerForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            return render('/')
    return render(request, 'update.html',{'form': form})

def read(request, id):
    q = programmer.objects.get(pk=id)
    return render(request, 'read.html', {'q':q})

def delete(request, id):
    programmer.objects.get(pk=id).delete()
    return render(request, 'delete.html')
def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password=password)
        
        if user is not None:

            login(request,user) 

            return redirect('/')  

    return render(request, 'login.html') 


def logoutt(request):
    logout(request)
    return redirect('/login') 

def signup(request):
    form = SignupForm()
    if request.method == 'POST':  
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'signup.html', {'form': form})




