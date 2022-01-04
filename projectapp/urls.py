from django.urls import path
from.views import ProjectApiView,ProjectDetailApiView

urlpatterns=[
    path('',ProjectApiView.as_view(),name='project_create'),
    path('<str:pk>/',ProjectDetailApiView.as_view(),name='project_detail')
]