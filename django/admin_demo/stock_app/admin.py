from django.contrib import admin

# Register your models here.
admin.site.site_header = "Stock Administration"
admin.site.site_title = "Stock Admin Portal"
admin.site.index_title = "Welcome to Stock Management Portal"
from .models import Stock
#@admin.register(Stock)
#admin.site.register(Stock,StockAdmin)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'price', 'volume', 'last_updated')
    search_fields = ('symbol', 'name')
    list_filter = ('last_updated',)
    ordering = ('-last_updated',)
admin.site.register(Stock, StockAdmin)