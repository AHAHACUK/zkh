from django.test import TestCase
from .models import Dispatcher
from tasks.models import Task
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


# Create your tests here.
class DispatcherTestCase(TestCase):
    def test_create(self):
        perm = Permission.objects.get(codename='view_task', content_type=ContentType.objects.get_for_model(Task))
        group, created = Group.objects.get_or_create(name='dispatcher')
        group.permissions.set([perm])
        group.save()
        user_created = Dispatcher.objects.create('woop', '112')
        user_created.save()
        user_got = User.objects.get(username='woop')
        self.assertEqual(user_created, user_got)
        self.assertTrue(user_created.groups.filter(name='dispatcher').exists())
        self.assertTrue(user_created.has_perm('tasks.view_task'))