from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import RolesView

router = routers.DefaultRouter()
router.register(r'workers', views.WorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me', RolesView.as_view())
]