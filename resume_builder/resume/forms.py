from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Resume

# class SignUpForm(forms.ModelForm):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password1 = forms.CharField()
#     password2 = forms.CharField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'full_name', 'email', 'phone', 'address', 'linkedin_profile', 'github_profile',
            'company_name', 'job_title', 'employment_dates', 'job_description',
            'institution_name', 'degree', 'attendance_dates', 'gpa',
            'programming_languages', 'web_frameworks', 'databases', 'cloud_platforms', 'soft_skills',
            'awards', 'projects'
        ]