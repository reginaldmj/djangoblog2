from django.shortcuts import render

from .models import Post

# Create your views here.

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/post-detail.html', context)
