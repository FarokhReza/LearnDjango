from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta: # create a model base project table in models.py
        model = Project
        # fields = '__all__' # name must be fields
        fields = ['title', 'featured_image', 'description', 
                  'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwards):
        super(ProjectForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            
        # self.fields['title'].widgets.attrs.update(
        #     {'class': 'input', 'placeholder': 'Add title'})
        # # for add project page and connect to css
        # self.fields['description'].widgets.attrs.update(
        #     {'class': 'input', 'placeholder': 'Add title'})

        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwards):
        super(ReviewForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})