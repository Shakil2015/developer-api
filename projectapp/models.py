from django.db import models
import uuid
from user.models import Profile
# Create your models here.

class Project(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    tags=models.ManyToManyField('Tag',blank=True)
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):

    VOTE_TYPE=(
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    #owner
    project=models.ForeignKey('Project',on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

class Tag(models.Model):
    
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Skill(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(max_length=1000,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    sender=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name='sender')
    receiver=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name='receiver')
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    body=models.TextField(max_length=1000,null=True,blank=True)
    is_read=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name