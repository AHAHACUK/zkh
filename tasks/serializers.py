import logging
import sys

from rest_framework import serializers

from .models import *


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    urgency = serializers.PrimaryKeyRelatedField(queryset=TaskUrgency.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=TaskStatus.objects.all())
    time_created = serializers.ReadOnlyField()
    time_updated = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['url', 'title', 'urgency', 'assigned_team', 'status', 'time_created', 'time_updated']


class ReportImageSerializer(serializers.ModelSerializer):
    src = serializers.ImageField(use_url=True)

    class Meta:
        model = ReportImage
        fields = ['src']


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    images = ReportImageSerializer(many=True)

    class Meta:
        model = Report
        fields = ['url', 'task', 'text', 'images']

    def create(self, validated_data):
        report = Report(
            task=validated_data['task'],
            text=validated_data['text']
        )
        report.save()
        for image in validated_data['images']:
            report_image = ReportImage(report=report, **image)
            report_image.save()
        return report
