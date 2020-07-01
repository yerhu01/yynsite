from django.shortcuts import render

from .models import About
from blog.models import Category, Post

# Create your views here.
def index(request):
    """The home page for yynsite."""
    title = "About Me"
    description = About.objects.order_by('-created_on')[0].description
    featured = Post.objects.filter(featured=True)[0:4]
    category = Category.objects.filter(name="Art")
    recent_art = Post.objects.filter(categories=category[0]).order_by('-created_on')[0:4]

    context = {
        'title': title,
        'description': description,
        'featured': featured,
        'recent_art': recent_art,
    }
    return render(request, 'index.html', context)


def art(request):
    """The art page for yynsite."""
    title = "My Art Timeline"
    category = Category.objects.filter(name="Art")
    post_list = Post.objects.filter(categories=category[0]).order_by('-created_on')

    context = {
        'title': title,
        'post_list': post_list,
    }
    return render(request, 'art.html', context)