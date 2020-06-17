from django.db import models

from django.urls import reverse
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField('Content')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})


def get_image_location(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  

class PostImage(models.Model):
    # When a Post is deleted, uploaded images are also deleted
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                related_name='images')
    image = models.ImageField(upload_to=get_image_location,
                                null=True, blank=True)
    
    def __str__(self):
        return "%s image" % (self.post.title)
    

