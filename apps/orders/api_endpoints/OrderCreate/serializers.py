from rest_framework import serializers

from apps.orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "car", "price", "status", "created_at")
        read_only_fields = ("id", "price", "status", "created_at")
