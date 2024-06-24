from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    
    # Work Experience
    company_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    employment_dates = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    
    # Education
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    attendance_dates = models.CharField(max_length=100, blank=True, null=True)
    gpa = models.CharField(max_length=10, blank=True, null=True)
    
    # Skills
    programming_languages = models.TextField(blank=True, null=True)
    web_frameworks = models.TextField(blank=True, null=True)
    databases = models.TextField(blank=True, null=True)
    cloud_platforms = models.TextField(blank=True, null=True)
    soft_skills = models.TextField(blank=True, null=True)
    
    # Awards and Honors
    awards = models.TextField(blank=True, null=True)
    
    # Projects
    projects = models.TextField(blank=True, null=True)
