from django.urls import path, re_path
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns

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

###API urls###
#####class based views
urlpatterns += format_suffix_patterns([
    path('api/blog/', views.ApiBlogList.as_view(), name='api-blog-list'),
    path('api/blog/detail/<int:pk>/', views.ApiBlogDetail.as_view(), name='api-blog-detail'),
    path('api/category/', views.ApiCategoryList.as_view(), name='api-category-list'),
    path('api/category/<int:pk>/', views.ApiCategoryDetail.as_view(), name='api-category-detail'),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),

    path('api/', views.api_root), #API root
    # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()), # snippet highlights
])