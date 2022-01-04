from django.shortcuts import render
from .models import Project,Skill,Message,Review,Tag
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ProjectSerializer


# Create your views here.
class ProjectApiView(ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
class ProjectDetailApiView(RetrieveUpdateDestroyAPIView):
    #queryset =Project.objects.all()
    serializer_class =ProjectSerializer

    def get_object(self):
        id=self.kwargs['pk']
        project= Project.objects.get(id=id)
        return project
    
    