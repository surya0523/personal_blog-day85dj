# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from ckeditor.widgets import CKEditorWidget
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'category',
            'tags',
            'image',
            'content',
            Submit('submit', 'Save Post', css_class='btn-primary mt-3')
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password',
            'password2',
            Submit('submit', 'Register', css_class='btn-success mt-3')
        )