from django import forms
from .models import diary
from django.contrib.auth.models import User


class ActiveForms(forms.ModelForm):

    activity = forms.CharField(max_length=200, label="Aktywność")
    emotions = forms.CharField(max_length=200, label="Nastrój")

    class Meta:
        model  = diary
        fields = ( "activity", "emotions")

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email')

class Dowland(forms.Form):
    Email = forms.EmailField()
    Name = forms.CharField(max_length=20)




