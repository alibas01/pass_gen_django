from django.shortcuts import render
from django.http import HttpResponse
import random
import copy

# Create your views here.

def home(request):
    return render(request, 'home.html', {'author': 'Ali Bas'})

def password(request):
    lowercase = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter = lowercase + uppercase
    length = int(request.GET.get('length', 9))
    special = list('!@#$%^&*()')
    nums = list('1234567890')
    #exception = copy.deepcopy(nums)
    word = copy.deepcopy(lowercase)
    passthe=random.choice(lowercase)

    if request.GET.get('uppercase'):
        word.extend(uppercase)
    if request.GET.get('special'):
        word.extend(special)
    if request.GET.get('numbers'):
        word.extend(nums)
    if request.GET.get('start'):
        passthe=random.choice(letter)
        length=length-1
    else:
        passthe=""


    for x in range(length):
        passthe += random.choice(word)


    return render(request, 'pass.html', {'password': passthe, 'author': 'Ali Bas'})



def about(request):
    return render(request, 'about.html', {'author': 'Ali Bas'})

def author(request):
    return HttpResponse('<h1>Author: <strong>Ali Bas</strong></h1>')

