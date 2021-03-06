from django.contrib import admin
from django.contrib.admin import display

from .models import Task, TaskService
from .models import Report
from .models import TaskUrgency
from .models import TaskStatus
from accounts.models import Worker


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['full_title', 'urgency', 'assigned_worker', 'status',
                    'time_assigned', 'time_closed', 'time_created', 'time_updated']
    list_filter = ['status']

    @display(description='Title')
    def full_title(self, obj):
        return obj


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskUrgency)
class TaskUrgencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'urgency']
    ordering = ['id']

@admin.register(TaskService)
class TaskServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'service']
    ordering = ['id']


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    ordering = ['id']
