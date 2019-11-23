from django import forms
from django.forms import ModelForm
from  django.contrib.auth.forms import UserCreationForm
from .models import UpdatePost


class UserCustomForm(UserCreationForm):
     pass

