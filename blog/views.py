from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.db.models import Q

from functools import reduce
from dal import autocomplete
from .models import Post, Comment, Category
from .forms import CommentForm, SearchForm

# Create your views here.
def blog_index(request):
    post_list = None
    if not request.user.is_superuser:
        post_list = Post.objects.all().exclude(private=True).order_by('-created_on')
    else:
        post_list = Post.objects.all().order_by('-created_on')

    form = SearchForm()

    context = {
        'post_list': post_list,
        'form': form,
    }
    return render(request, 'blog.html', context)

def blog_search(request):
    queryset = Post.objects.all()
    query = None
    category = None
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            query = form.cleaned_data["search"].split()
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            category = form.cleaned_data["category"]
            #end_date = end_date.replace(day=end_date.day+1)

            if category != 'All':
                queryset = queryset.filter(
                        categories__name__icontains=category
                        ).order_by(
                            '-created_on'
                        )
            queryset = queryset.filter(created_on__range=(start_date, end_date))
    
    if query:
        #Q(name__contains=list[0]) | Q(name__contains=list[1]) | ... | Q(name__contains=list[-1])
        queryset = queryset.filter(
                reduce(lambda x, y: x | y, [Q(title__contains=word) for word in query])|
                reduce(lambda x, y: x | y, [Q(overview__contains=word) for word in query])
                #Q(title__icontains=query)|
                #Q(overview__icontains=query)
                ).distinct() #does it have a title or overview that contains the query
                             #.distinct to avoid getting same post twice
                             
    
    context = {'queryset': queryset,
        'query': query,
        'category': category,
            }

    return render(request, 'search_results.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__icontains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.private == True:
        if not request.user.is_superuser:
            return HttpResponse("Sorry! You don't have access to that page")

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                user=request.user,
                #author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            #clears text/submission data from form
            return redirect(reverse("blog_detail", kwargs={
                'pk': pk,
            }))
    
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)

# class CategoryAutocompleteFromList(autocomplete.Select2ListView):
#     def get_list(self):
#         categories = ['All']
#         queryset = Category.objects.all()
#         for category in queryset:
#             categories.append(str(category))
#         return categories


