from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile/",default = "default.jpg")
    bio = HTMLField()
    updated_on = models.DateTimeField(auto_now_add=True)

class Project_Post(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    img_project = models.ImageField(upload_to="project/")
    project_url = models.URLField()
    description = HTMLField()
    posted_on = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    review = HTMLField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(Project_Post,on_delete=models.CASCADE)
    

class Rates(models.Model):
    rate = models.IntegerField(default = 0)
    rate_by = models.ForeignKey(User,on_delete=models.CASCADE)
    rate_on = models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(Project_Post,on_delete=models.CASCADE)
    
