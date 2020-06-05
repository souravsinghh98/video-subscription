from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CreateUserForm
from datetime import datetime, timedelta
from .filters import MovieFilter
from math import ceil

# Create your views here.
def home(request):
    movie = Movie.objects.all().order_by('-id')
    hollywood = Movie.objects.filter(category='Hollywood')
    bollywood = Movie.objects.filter(category='Bollywood')
    myFilter = MovieFilter(request.GET, queryset=movie)
    movie = myFilter.qs
    context = {'movies':movie,'myFilter':MovieFilter,'hollywood':hollywood, 'bollywood':bollywood}
    return render(request, 'membership/home.html', context)

@login_required(login_url='login')
def movie(request,pk):
    curr_movie = Movie.objects.get(id=pk)
    subscription = curr_movie.allowed_memberships
    context = {'movie':curr_movie}
    #user_groups = request.user.groups.all() 
     
    if request.user.groups.filter(name=str(subscription)).exists() or request.user.groups.filter(name='Gold').exists():
        
        return render(request, 'membership/movie.html', context)
    else:
        messages.info(request, 'Upgrade your subscription to access the content')
        return redirect('buy_subs')
    

    
       
@login_required(login_url='login')
def buy_subscription(request):
    memberships = Membership.objects.all().order_by('price')
    curr_user = UserMembership.objects.get(user=request.user)
    curr_user_membership = str(curr_user.membership)

    context = {'memberships':memberships, 'curr_user_membership':curr_user_membership}
    return render(request, 'membership/buy_subs.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                UserMembership.objects.create(
                    user = user
                )    
                free_group = Group.objects.get(name='Free')
                user.groups.add(free_group)
                messages.success(request, 'User created successfully.')
                return redirect('login')
        else:
            pass
    context = {'form':form}
    return render(request, 'membership/register.html', context)  

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            uname = request.POST['uname'] 
            pwd = request.POST['pwd']
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'Invalid username or password')


    return render(request, 'membership/login.html')    

def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def payment_page(request,slug):
    selected_membership = Membership.objects.get(slug=slug)
    context = {'memberships':selected_membership}
    return render(request, 'membership/payment.html', context)

@login_required(login_url='login')
def checkout(request, slug):
    membership = Membership.objects.get(slug=slug)
    curr_user = UserMembership.objects.get(user=request.user)
    membership_group = Group.objects.get(name=membership)
    request.user.groups.add(membership_group)
    curr_user.membership = membership
    curr_user.date_added = datetime.now().date()
    curr_user.save()
    messages.success(request, 'Payment successfull')
    return redirect('home')

@login_required(login_url='login')
def userProfile(request):
    curr_user = UserMembership.objects.get(user=request.user)
    membership = str(curr_user.membership)
    context = {'user':curr_user, 'membership':membership}
    return render(request, 'membership/profile.html', context)

@login_required(login_url='login')
def confirmCancel(request):
    return render(request, 'membership/cancel.html')

@login_required(login_url='login')
def cancel(request):
    curr_user = UserMembership.objects.get(user=request.user)
    free_mem = Membership.objects.get(membership_type='Free')
    curr_user.membership = free_mem
    curr_user.save()
    request.user.groups.clear()
    free_grp = Group.objects.get(name='Free')
    request.user.groups.add(free_grp)
    messages.success(request, 'Your membership has been cancelled.')
    return redirect('profile')
