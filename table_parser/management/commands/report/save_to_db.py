from .dategen import dategen
from table_parser.models import UrsipData
from datetime import datetime
from django.db.models import Sum
from tqdm import tqdm


def update_report():
    totals = UrsipData.objects.filter(
        date__month=datetime.now().month).values('date').annotate(
        total_qliq=
        Sum('fact_qliq_data1') +
        Sum('fact_qliq_data2') +
        Sum('forecast_qliq_data1') +
        Sum('forecast_qliq_data2'),
        total_qoil=
        Sum('fact_qoil_data1') +
        Sum('fact_qoil_data2') +
        Sum('forecast_qoil_data1') +
        Sum('forecast_qoil_data2')
    )
    for total in tqdm(totals):
        UrsipData.objects.filter(
            date=total['date']).update(total_qliq=total['total_qliq'],
                                       total_qoil=total['total_qoil']
                                       )


def save_report(data):
    for i, row in tqdm(data.iterrows()):
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
            date=dategen()
        )
        res.save()
    update_report()
