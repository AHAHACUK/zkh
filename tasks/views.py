from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics

from . import models
from . import serializers
from .models import Task


class TeamViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = []


class ReportViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = []


class TaskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = []


def report_image_media_access(request, task, image_index):
    if request.user.has_perm('tasks.view_report'):
        task = Task.objects.filter(pk=task).first()
        if task and task.report:
            images = task.report.images.all()
            if len(images) >= image_index:
                image = images[image_index - 1].src
                return FileResponse(image)
    return HttpResponseNotFound()
