from django.urls import path

from apps.orders.api_endpoints.OrderCreate.views import OrderCreateAPIview
from apps.orders.api_endpoints.OrderDetail.views import OrderDetailAPIview
from apps.orders.api_endpoints.OrderList.views import MyOrderListAPIview, OrderListAPIview


urlpatterns = [
    path('', OrderListAPIview.as_view(), name='order-list'),
    path('my/', MyOrderListAPIview.as_view(), name='my-order-list'),
    path('create/', OrderCreateAPIview.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailAPIview.as_view(), name='order-detail'),
]
