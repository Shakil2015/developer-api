from rest_framework import serializers
from .models import Project,Skill,Tag,Message

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'