from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .models import Order
from .serializers import OrderSerializer




class OrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.all()

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(order_date__range=[start_date, end_date])

        min_amount = self.request.query_params.get('min_amount')
        if min_amount:
            queryset = queryset.filter(total_amount__gte=min_amount)

        return queryset
