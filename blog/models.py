from django.db import models

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from datetime import date

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    date = models.DateField(default=date.today)
    created_on = models.DateTimeField(auto_now_add=True) #UTC
    content = HTMLField('Content', blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')
        #By adding a related_name of posts, we can access category.posts to give us a list of posts with that category
    featured = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})


def get_image_location(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%d-%s/%s" % (instance.post.pk, slug, filename)  

class PostImage(models.Model):
    # When a Post is deleted, uploaded images are also deleted
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                related_name='images') #can access by post.images in template
    image = models.ImageField(upload_to=get_image_location,
                                null=True, blank=True)
    
    def __str__(self):
        return "%s image" % (self.post.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.user.username

