from datetime import datetime

from django.db import models


# Create your models here.
class Team(models.Model):

    def __str__(self):
        return f'Team #{self.id}'


class TaskStatus(models.Model):
    status = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural='Task Statuses'

    def __str__(self):
        return self.status


class TaskUrgency(models.Model):
    urgency = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural='Task Urgencies'

    def __str__(self):
        return self.urgency


class Task(models.Model):
    title = models.CharField(max_length=30)
    urgency = models.ForeignKey(TaskUrgency, default=0, on_delete=models.SET_DEFAULT)
    assigned_team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    status = models.ForeignKey(TaskStatus, default=0, on_delete=models.SET_DEFAULT)
    time_created = models.TimeField(default=datetime.now)
    time_updated = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'#{self.id}: {self.title}'


class Report(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='report')
    text = models.TextField()
    time_created = models.TimeField(default=datetime.now)

    def __str__(self):
        return f'R#{self.task.id}: {self.title}'


def image_path(instance, filename):
    return f'reports/{instance.report.task.pk}/{filename}'


class ReportImage(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to=image_path)
