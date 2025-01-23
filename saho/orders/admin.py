from django.contrib import admin
from django.contrib import admin
from .models import Order




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'order_date', 'total_amount') 
    list_filter = ('status', 'order_date')  
    search_fields = ('customer__email', 'id')  
    date_hierarchy = 'order_date'  
    ordering = ('-order_date',)  
