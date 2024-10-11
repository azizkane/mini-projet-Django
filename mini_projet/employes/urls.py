from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeViewSet, DirigeantViewSet, CongeViewSet

router = DefaultRouter()
router.register(r'employes', EmployeViewSet)
router.register(r'dirigeants', DirigeantViewSet)
router.register(r'conges', CongeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
