import logging
import sys

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
from accounts.models import Worker


class ChoiceItemField(serializers.ChoiceField):

    def __init__(self, queryset, item_column, *args, **kwargs):
        self.queryset = queryset
        self.item_column = item_column
        choises = queryset.values_list(item_column, flat=True)
        super().__init__(choises, *args, **kwargs)

    def to_internal_value(self, data):
        keyargs = {self.item_column: data}
        item = self.queryset.filter(**keyargs).first()
        if item:
            return item
        else:
            raise ValidationError(f'Option does not exist: {data}')

    def to_representation(self, value):
        return getattr(value, self.item_column)


class TaskServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskService
        fields = ['service']


class TaskSerializer(serializers.ModelSerializer):
    urgency = ChoiceItemField(TaskUrgency.objects.all(), 'urgency')
    status = ChoiceItemField(TaskStatus.objects.all(), 'status')
    assigned_worker_id = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all(), source='assigned_worker', required=False)
    assigned_worker_name = serializers.SerializerMethodField('get_assigned_worker_name')
    time_created = serializers.ReadOnlyField()
    time_updated = serializers.ReadOnlyField()

    def get_assigned_worker_name(self, task):
        if task.assigned_worker:
            return task.assigned_worker.full_name()
        else:
            return None

    class Meta:
        model = Task
        fields = [
            'url', 'id', 'title', 'urgency', 'status',
            'address_desc', 'address_latitude', 'address_longitude',
            'assigned_worker_id', 'assigned_worker_name',
            'time_assigned', 'time_closed', 'time_created', 'time_updated'
        ]


class ReportImageSerializer(serializers.ModelSerializer):
    src = serializers.ImageField(use_url=True)

    class Meta:
        model = ReportImage
        fields = ['src']


class ReportSerializer(serializers.ModelSerializer):
    task_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), source='task')
    task = serializers.SerializerMethodField('get_task_str')
    images = ReportImageSerializer(many=True, required=False, allow_null=True)

    def get_task_str(self, report):
        return report.task.title

    class Meta:
        model = Report
        fields = ['url', 'id', 'task_id', 'task', 'text', 'images', 'time_created']

    def create(self, validated_data):
        report = Report(
            task=validated_data['task'],
            text=validated_data['text']
        )
        report.save()
        if 'images' in validated_data:
            for image in validated_data['images']:
                report_image = ReportImage(report=report, **image)
                report_image.save()
        return report
