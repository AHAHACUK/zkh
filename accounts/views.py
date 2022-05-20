from django import http
from django.shortcuts import render
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView

from . import models
from . import serializers


class WorkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Worker.objects.all()
    serializer_class = serializers.WorkerSerializer
    permission_classes = []

@method_decorator(csrf_exempt, name='dispatch')
class RolesView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            is_worker = hasattr(user, 'worker')
            is_dispatcher = hasattr(user, 'dispatcher')
            response_data = {
                'user_id': user.pk,
                'name': user.get_full_name(),
                'is_worker': is_worker,
                'is_dispatcher': is_dispatcher,
            }
            if is_worker:
                response_data['worker_id'] = user.worker.pk
            if is_dispatcher:
                response_data['dispatcher_id'] = user.dispatcher.pk
            return http.JsonResponse(response_data)
        else:
            return http.JsonResponse({'error': 'not authenticated'})
