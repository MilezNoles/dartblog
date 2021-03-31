from django import forms
from .models import *  # для выпадающего списка категорий
import re  # для clean_title
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# from captcha.fields import CaptchaField


# class ContactForm(forms.Form):
#     subject = forms.CharField(label="Тема",
#                               widget=forms.TextInput(attrs={'class': "form-control", }), )
#     content = forms.CharField(label="Текст",
#                               widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5}), )
#     captcha = CaptchaField()


class UserLogin(AuthenticationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={'class': "form-control", }), )
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={'class': "form-control", }))


class UserRegister(UserCreationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={'class': "form-control", }),
                               help_text="Mast be less than 150 chars")
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': "form-control", }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-control", }),
                                help_text="Longer than 8 chars (letters & nums)")
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput(attrs={'class': "form-control", }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # widgets = {"username" : forms.TextInput(attrs={'class': "form-control", }),
        #            "email": forms.EmailInput(attrs={'class': "form-control", }),
        #            "password1" : forms.PasswordInput(attrs={'class': "form-control", }),
        #            "password2": forms.PasswordInput(attrs={'class': "form-control", }),
        #
        # } для UserCreationForm это поле работает не корректно, поэтому все переносим из меты в UserRegister


# class CommentsForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ["nickname", "message", ]
#         widgets = {
#             "nickname": forms.TextInput(attrs={'class': "form-control", "type": "hidden"}, ),
#             "message": forms.Textarea(attrs={
#                 'class': "form-control",
#                 'rows': 5
#             }),
#
#         }