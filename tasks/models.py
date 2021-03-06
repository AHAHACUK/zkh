from datetime import datetime

from django.db import models


class TaskStatus(models.Model):
    status = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = 'Task Statuses'

    def __str__(self):
        return self.status


class TaskUrgency(models.Model):
    urgency = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = 'Task Urgencies'

    def __str__(self):
        return self.urgency


class TaskService(models.Model):
    service = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural='Task Services'

    def __str__(self):
        return self.service


class Task(models.Model):
    title = models.TextField()
    urgency = models.ForeignKey(TaskUrgency, default=0, on_delete=models.SET_DEFAULT)
    address_desc = models.CharField(max_length=64, blank=True, default='')
    address_latitude = models.FloatField(default=0)
    address_longitude = models.FloatField(default=0)
    assigned_worker = models.ForeignKey('accounts.Worker', null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    status = models.ForeignKey(TaskStatus, default=0, on_delete=models.SET_DEFAULT)
    service = models.ManyToManyField(TaskService)
    time_assigned = models.DateTimeField(blank=True, null=True)
    time_closed = models.DateTimeField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'#{self.id}: {self.title}'


class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reports')
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'R#{self.task.id}: {self.title}'


def image_path(instance, filename):
    return f'reports/{instance.report.task.pk}/{filename}'


class ReportImage(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to=image_path)
