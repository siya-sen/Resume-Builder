from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # Import pisa module from xhtml2pdf library
from .forms import SignUpForm, LoginForm, ResumeForm
from .models import Resume

def index(request):
    return render(request, "base.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
          
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def resume_form(request):
    resume, created = Resume.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('homepage')  # Redirect to the resume detail view after creation
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'resume_form.html', {'form': form})

@login_required
def resume_detail(request):
    resume = get_object_or_404(Resume, user=request.user)
    return render(request, 'resume_detail.html', {'resume': resume})

@login_required
def resume_template_elegant(request):
    resume = get_object_or_404(Resume, user=request.user)
    return render(request, 'resume_template_elegant.html', {'resume': resume})
@login_required
def resume_template_creative(request):
    resume = get_object_or_404(Resume, user=request.user)
    return render(request, 'resume_template_creative.html', {'resume': resume})
@login_required
def resume_template_minimalist(request):
    resume = get_object_or_404(Resume, user=request.user)
    return render(request, 'resume_template_minimalist.html', {'resume': resume})
@login_required
def resume_template_modern(request):
    resume = get_object_or_404(Resume, user=request.user)
    return render(request, 'resume_template_modern.html', {'resume': resume})
    

@login_required
def resume_pdf(request):
    resume = request.user.resume
    template_path = 'resume_pdf.html'
    context = {'resume': resume}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    
    # Use pisa to create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='utf-8')
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def homepage(request):
    resume=Resume.objects.all()
    return render(request, 'homepage.html', {'resume': resume})

@login_required
def template_page(request):
    resume=Resume.objects.all()
    return render(request, 'template_page.html', {'resume': resume})


@login_required
def edit_resume(request):
    resume = get_object_or_404(Resume, user=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('homepage')  # Redirect to the resume detail view after creation
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'edit_resume.html', {'resume': resume})
    