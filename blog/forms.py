from django import forms
# from tinymce import TinyMCE
from datetime import date
from .models import Post, Category
from dal import autocomplete

# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False

# class PostForm(forms.ModelForm):
#     content = forms.CharField(
#             widget=TinyMCEWidget(
#                 attrs={'required': False, 'cols': 30, 'rows': 10}
#             )
#     )

#     class Meta: 
#         model = Post
#         fields =  ('title', 'overview', 'content', 'thumbnail', 
#                 'categories', 'featured', 'previous_post', 'next_post')
#                     #'__all__'

def get_choice_list():
    categories = ['All']
    queryset = Category.objects.all()
    for category in queryset:
        categories.append(str(category))
        
    return categories

class SearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Search blog",
        })
    )
    category = autocomplete.Select2ListChoiceField(
        choice_list=get_choice_list,
        widget=autocomplete.ListSelect2() #url='category-autocomplete')
    )
    start_date = forms.DateField(initial=date(2020,1,1))
    end_date = forms.DateField(initial=date.today)


class CommentForm(forms.Form):
    # author = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Your Name"
    #     })
    # )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!",
            'rows': '4',
        })
    )
