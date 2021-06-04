from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html', {'author': 'Ali Bas'})

def password(request):
    lowercase = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    length = int(request.GET.get('length', 9))
    special = list('!@#$%^&*()')
    nums = ('1234567890')
    word = ''
    passthe=""

    if request.GET.get('uppercase'):
        lowercase.extend(uppercase)
    if request.GET.get('special'):
        lowercase.extend(special)
    if request.GET.get('numbers'):
        lowercase.extend(nums)
    if request.GET.get('uppercase'):
        lowercase.extend(uppercase)

    for x in range(length):
        passthe += random.choice(lowercase)

    return render(request, 'pass.html', {'password': passthe, 'author': 'Ali Bas'})





def author(request):
    return HttpResponse('<h1>Author: <strong>Ali Bas</strong></h1>')

