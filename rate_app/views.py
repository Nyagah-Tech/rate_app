from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import Post_projectform,ReveiwForm
from django.contrib import messages
from .models import Project_Post,Profile,Reviews,Rates


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
    
@login_required
def post_review_view(request,id):
    
    form = ReveiwForm()
    reviews = Reviews.get_review_by_project_id(id)
    project = Project_Post.get_project_by_id(id)
    rates = Rates.get_rates_by_project_id(id)
    desrate = []
    usarate=[]
    conrate=[]
    for rate in rates:
        desrate.append(rate.design)
        usarate.append(rate.usability)
        conrate.append(rate.content)
    total = len(desrate)*9
    design =round(sum(desrate)/total *100,2)
    usability = round(sum(usarate)/total *100,2)
    content = round(sum(conrate),2)
        
    return render(request,'all/single_project.html',{"form":form,"reviews":reviews,"project":project,"project_id":id,"design":design,"usability":usability,"content":content})
 

            
    