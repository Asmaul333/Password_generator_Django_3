from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

# def home(request):
#    return HttpResponse('Wellcome to Batman World.')
def home(request):
    return render(request, 'Password/home.html')

def Password(request):
    mypassword = ''
    charecters=list('abcdefghijklmnopqrstuvwxyz')
    numbers=list('1234567890')
    special_charecters=list('!@#$%^&*()_')
    uppercase=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    length=int(request.GET.get('length'))

    if request.GET.get('UpperCase'):
        charecters.extend(uppercase)
    if request.GET.get('Numbers'):
        charecters.extend(numbers)
    if request.GET.get('Special Charecter'):
        charecters.extend(special_charecters)

    for x in range(length):
        mypassword+=random.choice(charecters)


    return render(request, 'Password/Password.html', {'Password':mypassword})

def about(request):
    return render(request, 'Password/about.html')
