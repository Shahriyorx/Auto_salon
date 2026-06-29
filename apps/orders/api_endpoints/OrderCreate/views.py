from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.orders.api_endpoints.OrderCreate.serializers import OrderCreateSerializer
from apps.orders.models import Order


class OrderCreateAPIview(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        car = serializer.validated_data["car"]
        serializer.save(user=self.request.user, price=car.price)
