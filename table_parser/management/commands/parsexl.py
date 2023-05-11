from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum
from table_parser.models import UrsipData
import pandas as pd
from datetime import datetime
from random import randint


class Command(BaseCommand):
    help = "Parse excel file"

    def table_update(self):
        totals = UrsipData.objects.filter(date__month=datetime.now().month).values('date').annotate(
            total_qliq=Sum('fact_qliq_data1') + Sum('fact_qliq_data2') + Sum('forecast_qliq_data1') + Sum(
                'forecast_qliq_data2'),
            total_qoil=Sum('fact_qoil_data1') + Sum('fact_qoil_data2') + Sum('forecast_qoil_data1') + Sum(
                'forecast_qoil_data2'))
        for total in totals:
            UrsipData.objects.filter(date=total['date']).update(total_qliq=total['total_qliq'],
                                                                total_qoil=total['total_qoil'])

        print(result)

    def handle(self, *args, **options):
        date = datetime(2023, 5, randint(1, 10))
        data = pd.read_excel(r'table_parser/src/table.xlsx', header=[0, 2], engine='openpyxl')
        data.columns = ['_'.join(col).strip() for col in data.columns.values]
        for i, row in data.iterrows():
            print(row)
            res = UrsipData(
                company=row['company_Unnamed: 1_level_1'],
                fact_qliq_data1=row['fact_data1'],
                fact_qliq_data2=row['fact_data2'],
                fact_qoil_data1=row['fact_data1.1'],
                fact_qoil_data2=row['fact_data2.1'],
                forecast_qliq_data1=row['forecast_data1'],
                forecast_qliq_data2=row['forecast_data2'],
                forecast_qoil_data1=row['forecast_data1.1'],
                forecast_qoil_data2=row['forecast_data2.1'],
                date=date
            )
            res.save()
        self.table_update()


from django.db.models import Sum
from datetime import datetime

# Рассчитать общий объем Qliq и Qoil для каждой даты
totals = UrsipData.objects.filter(date__month=datetime.now().month).values('date').annotate(
    total_qliq=Sum('fact_qliq_data1') + Sum('fact_qliq_data2') + Sum('forecast_qliq_data1') + Sum(
        'forecast_qliq_data2'),
    total_qoil=Sum('fact_qoil_data1') + Sum('fact_qoil_data2') + Sum('forecast_qoil_data1') + Sum(
        'forecast_qoil_data2'))

# Сохранить рассчитанные значения в базу данных
for total in totals:
    UrsipData.objects.filter(date=total['date']).update(total_qliq=total['total_qliq'], total_qoil=total['total_qoil'])
