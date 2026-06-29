from rest_framework import serializers

from apps.orders.models import Order


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "user", "car", "price", "status", "created_at", "updated_at")
        read_only_fields = fields
