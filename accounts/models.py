from django.db import models
from django.contrib.auth.models import User


class Dispatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dispatcher')

    def __str__(self):
        return self.user.get_full_name()


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker')

    def __str__(self):
        return self.user.get_full_name()
