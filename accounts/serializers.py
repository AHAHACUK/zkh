from rest_framework import serializers

from .models import *


class WorkerSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, source='user')
    class Meta:
        model = Worker
        fields = ['id', 'user_id', 'full_name', 'specialization']