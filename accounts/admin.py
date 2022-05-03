from django.contrib import admin
from accounts.models import Worker
from accounts.models import Dispatcher
from django.contrib.admin import display


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'team']

    @display(description='Full name')
    def user_full_name(self, obj):
        return obj.user.get_full_name()


@admin.register(Dispatcher)
class DispatcherAdmin(admin.ModelAdmin):
    pass
