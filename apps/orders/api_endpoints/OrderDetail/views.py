from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.orders.api_endpoints.OrderDetail.serializers import OrderDetailSerializer
from apps.orders.models import Order


class OrderDetailAPIview(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.select_related("user", "car")
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
