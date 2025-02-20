from django.contrib import admin
from .models import StockPrediction

@admin.register(StockPrediction)
class StockPredictionAdmin(admin.ModelAdmin):
    list_display = ("open_price", "high", "low", "pe_ratio", "pb_ratio", "dividend_yield", "predicted_close_price", "created_at")
    list_filter = ("created_at",)
    search_fields = ("open_price", "high", "low", "predicted_close_price")

