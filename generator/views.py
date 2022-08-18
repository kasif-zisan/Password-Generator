from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    combination = string.ascii_lowercase
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        combination+=string.ascii_uppercase
    if request.GET.get('numbers'):
        combination+='0123456789'
    if request.GET.get('characters'):
        combination+=string.punctuation
    thepass = ''
    for x in range(length):
        thepass+=random.choice(combination)
    return render(request,'generator/password.html',{'pa' : thepass})

def about(request):
    return render(request, 'generator/about.html')
def socials(request):
    if request.GET.get('facebook'):
        facebook=''
        facebook = "https://www.facebook.com/Zisan.Rocks"
    return render(request,'generator/socials.html',{'link' : facebook})