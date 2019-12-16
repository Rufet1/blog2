from django.shortcuts import render,redirect,Http404
from .models import UserProfil
from .forms import ProfilForm
from django.contrib.auth.models import User
# Create your views here.

def add_image(request):
    form = ProfilForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        if not request.user.userprofil.image:
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect ('home')
        else:
            return redirect('home')
    return render (request, 'profil/form.html', {'form':form})

def profil_view(request):
    if not request.user.is_authenticated:
        return Http404
    return render(request,'profil/profil.html')

def profiles(request):
    profiles = User.objects.all()
    return render(request,'profil/index.html', {'profiles':profiles})

def contact(request):
    return render(request, 'contact.html')