from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from .models import Ad, ExchangeProposal
from .serializers import AdSerializer, ExchangeProposalSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by("-created_at")
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExchangeProposalViewSet(viewsets.ModelViewSet):
    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # временная заглушка
        serializer.save(ad_sender=self.request.user.ads.first())
