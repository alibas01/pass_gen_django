from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'author': 'Ali Bas'})

def password(request):
    passthe="The password"
    return render(request, 'pass.html', {'password': passthe})





def author(request):
    return HttpResponse('<h1>Author: <strong>Ali Bas</strong></h1>')

