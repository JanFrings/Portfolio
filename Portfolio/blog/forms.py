from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm




class UserForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = 'NAME'
        # self.fields['email'].label = 'NAME'



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'mentor', 'image', 'url')


# allows the user to edit there text input
    widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

# allows the user to edit there text input
    widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
