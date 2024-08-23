from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CoursesForms, CustomUser

# User Registration Form should use CustomUser model
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# User Login Form
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# Profile Form should use Profile model, not CustomUser
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'resume', 'resume_headline']

# Courses Forms Form
class CoursesFormsForm(forms.ModelForm):
    class Meta:
        model = CoursesForms
        fields = ['name', 'email', 'phone_number', 'looking_for', 'agree_terms', 'course_name']
