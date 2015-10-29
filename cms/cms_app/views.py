# -*- coding: utf-8 -*-
from cms_app.models import Column, Article

from django.shortcuts import redirect

from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})
 
 
def article_detail(request,pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article': article})

def aboutus(request):
    return render(request, 'aboutus/index.html')





def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login_.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:
                return render_to_response('login_.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('login_.html', RequestContext(request, {'form': form,}))

def register(request):
    errors= []
    account=None
    password=None
    password2=None
    email=None
    CompareFlag=False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password= request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('Please Enter password2')
        else:
            password2= request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('Please Enter email')
        else:
            email= request.POST.get('email')

        if password is not None and password2 is not None:
            if password == password2:
                CompareFlag = True
            else :
                errors.append('password2 is diff password ')


        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag :
            user=User.objects.create_user(account,email,password)
            user.is_active=True
            user.save
            return HttpResponseRedirect('accounts/login')
    return render(request,'register.html', {'errors': errors})



@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("accounts/login/")