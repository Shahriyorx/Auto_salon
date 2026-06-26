from rest_framework.pagination import LimitOffsetPagination

class CarLimitOffsetpagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 100