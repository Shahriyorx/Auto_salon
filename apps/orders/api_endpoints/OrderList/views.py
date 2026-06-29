from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.orders.api_endpoints.OrderList.serializers import OrderListSerializer
from apps.orders.models import Order


class OrderListAPIview(generics.ListAPIView):
    queryset = Order.objects.select_related("user", "car").all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAdminUser]


class MyOrderListAPIview(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.select_related("user", "car").filter(user=self.request.user)
