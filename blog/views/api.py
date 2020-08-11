from blog.models import Post, Category
from blog.serializers import (PostListSerializer, PostDetailSerializer,
                            CategoryListSerializer, CategoryDetailSerializer)
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiBlogList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class ApiBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    #IsAuthenticatedOrReadOnly, which will ensure that authenticated requests 
    # get read-write access, and unauthenticated requests get read-only access.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                         IsOwnerOrReadOnly]

class ApiCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class ApiCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'blog': reverse('api-blog-list', request=request, format=format),
        'category': reverse('api-category-list', request=request, format=format),
    })