from rest_framework import serializers
from blog.models import Post, Category

class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-category-detail')

    class Meta:
        model = Category
        fields = ['id', 'name', 'url']

class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='api-blog-detail', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-blog-detail')
    categories =  CategoryListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'overview', 'date', 'categories']


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    categories =  CategoryListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'overview', 'date', 'content', 'featured', 'private', 'categories']


