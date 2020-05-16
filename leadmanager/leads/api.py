from leads.models import Lead
from rest_framwork import viewsets, permissions
from .serializers import LeadSerializer

# Viewset


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer
