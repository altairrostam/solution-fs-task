from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GetEmailSerializer, PatchEmailSerializer
from .models import Email


class EmailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Email.objects.all().order_by('-timestamp')
    serializer_class = PatchEmailSerializer
    permission_classes = [permissions.IsAuthenticated]