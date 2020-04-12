from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    charecters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    password = ''

    if request.GET.get('upppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        charecters.extend(list('0123456789'))

    if request.GET.get('special'):
        charecters.extend(list('~!@#$%^&*'))

    for i in range(length):
        password += random.choice(charecters)

    return render(request,'generator/password.html',{'password':password})

def about(request):

    return render(request,'generator/about.html')
