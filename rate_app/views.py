from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,"all/index.html")

def logout_view(request):
    logout(request)
    return redirect('/')
    
# Create your views here.
