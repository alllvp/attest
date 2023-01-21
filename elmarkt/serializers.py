from rest_framework import serializers
from .models import Participant, Supplier


class ParticipantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        read_only_fields = ("id", "created")
        fields = "__all__"


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = "__all__"
        read_only_fields = ("id", "created")


class SupplierCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        read_only_fields = ["id"]
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ("id", "debt")
