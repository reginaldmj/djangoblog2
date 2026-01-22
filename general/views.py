from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'general/home.html')

def about(request):
    return render(request, 'general/about.html')

def contact(request):
    return render(request, 'general/contact.html')