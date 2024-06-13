from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Cheatsheet, News
from django.views.decorators.http import require_GET

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def news(request):
    return render(request, 'main/news.html')

def rules(request):
    files = Cheatsheet.objects.all()
    print(files)
    context = {
        'files' : files
    }
    return render (request, 'main/rules.html', context)


import mimetypes
from django.http import FileResponse
from django.shortcuts import get_object_or_404

def download_cheatsheet(request, cheatsheet_id):
    cheatsheet = get_object_or_404(Cheatsheet, pk=cheatsheet_id)
    file_path = cheatsheet.file.path

    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = 'application/octet-stream'  

    file = open(file_path, 'rb')
    
    response = FileResponse(file, content_type=content_type)
    
    response['Content-Disposition'] = f'attachment; filename="{cheatsheet.title}{file_path[-5:]}"'
    
    return response
 
def cheatsheet(request):
    files = Cheatsheet.objects.all()
    print(files)
    context = {
        'files' : files
    }
    return render(request, 'main/index.html', context)

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /index/",
        "Allow: /about/",
        "Allow: /news/",
        "Allow: /rules/",
        "Disallow: /login/",
        "Disallow: /custom_admin_dashboard/",
        "Disallow: /manage_news/",
        "Disallow: /add_news/",
        "Disallow: /edit_news/",
        "Disallow: /delete_news/",
        "Disallow: /manage_cheatsheets/",
        "Disallow: /add_cheatsheet/",
        "Disallow: /edit_cheatsheet/",
        "Disallow: /delete_cheatsheet/",
        "Disallow: /logout/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def my_custom_page_not_found_view(request, exception):
    return render(request, 'main/404.html', {}, status=404)


from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news = News.objects.all().order_by('-published_date')
    return render(request, 'main/news.html', {'news': news})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'main/news_detail.html', {'news': news_item})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewsForm, CheatsheetForm
from .models import News, Cheatsheet

@login_required
def custom_admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('index')
    return render(request, 'custom_admin/dashboard.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Cheatsheet

@login_required
def manage_news(request):
    if not request.user.is_staff:
        return redirect('index')
    news = News.objects.all()
    return render(request, 'custom_admin/manage_news.html', {'news': news})

@login_required
def add_or_edit_news(request, news_id=None):
    if not request.user.is_staff:
        return redirect('index')
    if news_id:
        news = get_object_or_404(News, id=news_id)
    else:
        news = News()
    if request.method == 'POST':
        news.title = request.POST.get('title')
        news.content = request.POST.get('content')
        news.image = request.FILES.get('image')
        news.save()
        return redirect('manage_news')
    return render(request, 'custom_admin/edit_news.html', {'news': news})

@login_required
def delete_news(request, news_id):
    if not request.user.is_staff:
        return redirect('index')
    news = get_object_or_404(News, id=news_id)
    news.delete()
    return redirect('manage_news')
@login_required
def manage_cheatsheets(request):
    if not request.user.is_staff:
        return redirect('index')
    cheatsheets = Cheatsheet.objects.all()
    return render(request, 'custom_admin/manage_cheatsheets.html', {'cheatsheets': cheatsheets})
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cheatsheet

@login_required
def add_or_edit_cheatsheet(request, cheatsheet_id=None):
    if not request.user.is_staff:
        return redirect('index')
    if cheatsheet_id:
        cheatsheet = get_object_or_404(Cheatsheet, id=cheatsheet_id)
    else:
        cheatsheet = Cheatsheet()  

    if request.method == 'POST':
        cheatsheet.title = request.POST.get('title')
        cheatsheet.file = request.FILES.get('file')
        cheatsheet.save()
        return redirect('manage_cheatsheets')
    return render(request, 'custom_admin/edit_cheatsheet.html', {'cheatsheet': cheatsheet})

@login_required
def delete_cheatsheet(request, cheatsheet_id):
    if not request.user.is_staff:
        return redirect('index')
    cheatsheet = get_object_or_404(Cheatsheet, id=cheatsheet_id)
    cheatsheet.delete()
    return redirect('manage_cheatsheets')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('custom_admin_dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'custom_admin/login.html', {'form': form})
