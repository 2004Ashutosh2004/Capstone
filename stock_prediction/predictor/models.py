from django.db import models

class StockPrediction(models.Model):
    open_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    pe_ratio = models.FloatField()
    pb_ratio = models.FloatField()
    dividend_yield = models.FloatField()
    predicted_close_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction at {self.created_at}: {self.predicted_close_price}"
