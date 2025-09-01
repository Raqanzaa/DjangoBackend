from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SavingsPlan
from .serializers import SavingsPlanSerializer

class SavingsPlanViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return SavingsPlan.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)