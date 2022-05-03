from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete

from accounts.models import Dispatcher
from accounts.models import Worker

groups = {
    Dispatcher: 'dispatcher',
    Worker: 'worker'
}


def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        group = Group.objects.get(name=groups[sender])
        user.is_staff = True
        user.groups.add(group)
        user.save()


def remove_user_from_group(sender, instance, **kwargs):
    user = instance.user
    group = Group.objects.get(name=groups[sender])
    user.groups.remove(group)
    user.save()


for k, v in groups.items():
    post_save.connect(add_user_to_group, sender=k)
    pre_delete.connect(remove_user_from_group, sender=k)
