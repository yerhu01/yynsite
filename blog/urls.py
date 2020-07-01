from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("search/", views.blog_search, name="blog_search"),
    # re_path(
    #     r'^category-autocomplete/$',
    #     views.CategoryAutocompleteFromList.as_view(),
    #     name='category-autocomplete',
    # ),
]