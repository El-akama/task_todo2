from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder": "Enter password",}))
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder": "Enter password confirmation",}))

    class Meta:
        model = User
        fields = ('username', 'email','password', 'password_confirmation')
        help_texts = {
            'username': None,
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', "placeholder": "Enter username",}),
            'email': forms.EmailInput(attrs={'class':'form-control', "placeholder": "example@email.com"}),
        }


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username already exists')
        return username

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('password not equal')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }
))