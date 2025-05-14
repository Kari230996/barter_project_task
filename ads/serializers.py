from rest_framework import serializers
from .models import Ad, ExchangeProposal


class AdSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ad
        fields = [
            "id",
            "user",
            "title",
            "description",
            "image_url",
            "category",
            "condition",
            "created_at"
        ]


class ExchangeProposalSerializer(serializers.ModelSerializer):
    ad_sender = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = ExchangeProposal
        fields = [
            "id",
            "ad_sender",
            "ad_receiver",
            "comment",
            "status",
            "created_at"
        ]
