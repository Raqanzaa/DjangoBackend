from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingsPlanViewSet

router = DefaultRouter()
router.register(r'savings', SavingsPlanViewSet, basename="savings")

urlpatterns = [
    path('', include(router.urls)),
]