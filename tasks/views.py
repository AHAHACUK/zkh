from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics

from . import models
from . import serializers
from .models import Task


class ReportViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = serializers.ReportSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = models.Report.objects.all()
        task_id = self.request.query_params.get('task_id')
        if task_id:
            queryset = queryset.filter(task__id=task_id)
        return queryset


class TaskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = serializers.TaskSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = models.Task.objects.all()
        worker_id = self.request.query_params.get('worker_id')
        if worker_id:
            queryset = queryset.filter(assigned_worker__id=worker_id)
        return queryset


def report_image_media_access(request, task, image_index):
    if request.user.has_perm('tasks.view_report'):
        task = Task.objects.filter(pk=task).first()
        if task and task.report:
            images = task.report.images.all()
            if len(images) >= image_index:
                image = images[image_index - 1].src
                return FileResponse(image)
    return HttpResponseNotFound()
