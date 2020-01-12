from rest_framework import serializers
from .models import Project_Post,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_pic','bio','updated_on')
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Post
        fields =('posted_by','img_project','project_url','description','posted_on','title')