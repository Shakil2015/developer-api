from django.contrib import admin
from projectapp.models import Project,Tag,Skill,Message,Review

admin.site.register([Message,Review,Skill,Tag,Project])

# Register your models here.
