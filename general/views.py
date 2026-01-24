from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'general/home.html', context)

def about(request):
    return render(request, 'general/about.html')

def contact(request):
    return render(request, 'general/contact.html')