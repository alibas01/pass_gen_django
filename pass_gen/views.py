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
    passthe=""
    reference = request.GET.get('reference', "")

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

    def mix(stri):
        result = ''
        counter = 0
        mixwords = ['A','a','e','E','o','O','l','L','s','S','B', 'i', 'I']
        for char in stri:
            if char not in mixwords and len(result)<4:
                result += char
            elif char not in mixwords and counter/len(result)<0.4:
                result += random.choice(word)
            elif char not in mixwords:
                result += char                
            else:
                if char=='A':
                    result += "4"
                    counter +=1
                if char=='a':
                    result += "@"
                    counter +=1
                if char=='B':
                    result += "8"
                    counter +=1
                if char=='e' or char=='E':
                    result += "3"
                    counter +=1
                if char=='o' or char=='O':
                    result += "0"
                    counter +=1
                if char=='l' or char=='L':
                    result += "1"
                    counter +=1
                if char=='s' or char=='S':
                    result += "$"
                    counter +=1
                if char=='i' or char=='I':
                    result += "!"
                    counter +=1
        return result

    if len(reference)==0:
        for x in range(length):
            passthe += random.choice(word)
    else:
        passthe=mix(reference)

    return render(request, 'pass.html', {'password': passthe, 'author': 'Ali Bas', 'reference':reference})

def about(request):
    return render(request, 'about.html', {'author': 'Ali Bas'})

def author(request):
    return HttpResponse('<h1>Author: <strong>Ali Bas</strong></h1>')

