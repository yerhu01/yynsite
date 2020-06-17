from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def blog(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list,
    }
    return render(request, 'blog.html', context)

def post(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post,
    }
    return render(request, 'post.html', context)

