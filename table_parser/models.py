from django.db import models


# Create your models here.

class UrsipData(models.Model):
    company = models.CharField(max_length=100)
    fact_qliq_data1 = models.IntegerField()
    fact_qliq_data2 = models.IntegerField()
    fact_qoil_data1 = models.IntegerField()
    fact_qoil_data2 = models.IntegerField()
    forecast_qliq_data1 = models.IntegerField()
    forecast_qliq_data2 = models.IntegerField()
    forecast_qoil_data1 = models.IntegerField()
    forecast_qoil_data2 = models.IntegerField()
    date = models.DateField(null=True)
    total_qliq = models.IntegerField(null=True)
    total_qoil = models.IntegerField(null=True)

    def __str__(self):
        return self.company
