from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,"all/index.html")


# Create your views here.
