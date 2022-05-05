from django.db import models
from django.contrib.auth.models import User


class Dispatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dispatcher')

    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.full_name()


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker')
    specialization = models.CharField(max_length=30, default='Не указана')

    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.full_name()
