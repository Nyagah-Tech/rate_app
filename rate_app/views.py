from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import Post_projectform
from django.contrib import messages
from .models import Project_Post,Profile,Reviews


@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project_Post.get_all_projects()
    return render(request,"all/index.html",{"projects":projects})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def post_project_view(request):
    if request.method =='POST':
        form = Post_projectform(request.POST,request.FILES)
        
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.posted_by = request.user
            new_project.save()
            return redirect('home')
        else:
            messages.info(request,'all fields are required')
            return redirect('post-project')
    
    else:
        form = Post_projectform()
    return render(request,'all/new_post.html',{"form":form})
    

            
        
    
    
# Create your views here.
