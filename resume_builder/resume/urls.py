
from django.urls import path
from resume import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('resume_form/', views.resume_form, name='resume_form'),
    path('homepage/', views.homepage, name='homepage'),
    path('edit_resume/', views.edit_resume, name='edit_resume'),
    path('resume_detail/', views.resume_detail, name='resume_detail'),
    path('resume_pdf/', views.resume_pdf, name='resume_pdf'),
    path('template_page/', views.template_page, name='template_page'),
    path('resume_template_elegant/', views.resume_template_elegant, name='resume_template_elegant'),
    path('resume_template_creative/', views.resume_template_creative, name='resume_template_creative'),
    path('resume_template_minimalist/', views.resume_template_minimalist, name='resume_template_minimalist'),
    path('resume_template_modern/', views.resume_template_modern, name='resume_template_modern'),
]
