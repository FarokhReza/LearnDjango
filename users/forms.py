from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Messages

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name', # change the first_name to Name in frontend
        }

    def __init__(self, *args, **kwards):  # refrence to form in login_register.html
        super(CustomUserCreationForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'short_intro', 'location', 'social_website'
                  , 'social_youtube', 'social_linkedin', 'social_github', 'social_twitter', 'profile_image']
        # exclude = ['field_to_exclude1', 'field_to_exclude2']

    def __init__(self, *args, **kwards):  
        super(ProfileForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']
        # fields = ['name', 'description']

    def __init__(self, *args, **kwards):  
        super(SkillForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwards):  
        super(MessageForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})