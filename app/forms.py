# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'password1', 'password2', 'phone_number', 'resume', 'resume_headline']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



    from django import forms
from .models import CoursesForms

class CoursesFormsForm(forms.ModelForm):
    class Meta:
        model = CoursesForms
        fields = ['name', 'email', 'phone_number', 'looking_for', 'agree_terms', 'course_name']

