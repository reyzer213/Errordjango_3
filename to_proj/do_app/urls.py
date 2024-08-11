from django.urls import path 
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('to_proj/<int:task_id>/',  views.task_detail, name='task_detail'),
    path('to_proj/new/',  views.task_detail, name='task_create'),
    path('to_proj/<int:task_id>/edit/',  views.task_detail, name='task_edit'),
    path('to_proj/<int:task_id>/delete/',  views.task_detail, name='task_delete'),
]