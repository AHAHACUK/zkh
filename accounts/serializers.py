from rest_framework import serializers

from .models import *


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['url', 'full_name', 'specialization']