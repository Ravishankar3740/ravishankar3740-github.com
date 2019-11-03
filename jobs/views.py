from django.shortcuts import render
from .models import Job
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
#{% url 'login' %}
def home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{ "jobs":jobs})


def login(request):
    if request.method == "POST":
        # check if a user exists
        # with the username and password
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'jobs/login.html', {'error': "Invalid Login credentials."})
    else:
        return render(request, 'jobs/login.html')

def signup(request):
    if request.method == "POST":
        # to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            # both the passwords matched
            # now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'jobs/register.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username= request.POST['username'],password= request.POST['password'])
                # this line cal login the user right no
                auth.login(request, user)
                return redirect(login)
        else:
            return render(request, 'jobs/register.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'jobs/register.html')

def logout(request):
    auth.logout(request)
    return redirect(login)
