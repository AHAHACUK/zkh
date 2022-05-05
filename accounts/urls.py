from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'workers', views.WorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]