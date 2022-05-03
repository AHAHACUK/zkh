from django.db import models
from django.contrib.auth.models import User
from tasks.models import Team


class Dispatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dispatcher')

    def __str__(self):
        return self.user.get_full_name()


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker')
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='workers')

    def __str__(self):
        return self.user.get_full_name()
