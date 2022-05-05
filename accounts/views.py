from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from . import models
from . import serializers


class WorkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Worker.objects.all()
    serializer_class = serializers.WorkerSerializer
    permission_classes = []