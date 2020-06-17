from django.shortcuts import render

from .models import About

# Create your views here.
def index(request):
    """The home page for yynsite."""
    title = "About Me"
    description = About.objects.order_by('-timestamp')[0].description

    context = {
        'title': title,
        'description': description,
    }
    return render(request, 'index.html', context)

def contact(request):
    """The contact page for yynsite."""
    title = "Send your message"
    context = {
        'title': title,
    }
    return render(request, 'contact.html', context)

def art(request):
    """The art page for yynsite."""
    title = "My Art Timeline"
    context = {
        'title': title,
    }
    return render(request, 'art.html', context)