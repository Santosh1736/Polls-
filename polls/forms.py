from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name= forms.CharField(max_length=30, required=False,help_text='Optional.')
    last_name= forms.CharField(max_length=30, required=False,help_text='Optional.')
    email= forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=30, help_text="Required.",label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, help_text="Required. It must match with above password",label='Confirm password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
