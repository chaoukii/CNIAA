from django import forms
from django.forms import TextInput
from workshop.models import Comment, Submit, Speciality
from django.contrib.auth.models import User
from .fields import GroupedModelChoiceField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "address", "text")

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "email")
        help_texts = {
            'username': None,
            'email': None,
        }


class SubmitForm(forms.ModelForm):
    speciality = GroupedModelChoiceField(
        queryset=Speciality.objects.exclude(parent=None),
        choices_groupby='parent'
    )
    class Meta:
        model = Submit
        fields = ('full_name','phone','speciality','article')
