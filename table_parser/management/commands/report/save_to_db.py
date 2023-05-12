from django.db.models import Sum
from table_parser.models import UrsipData
from tqdm import tqdm
from datetime import datetime
from random import randint


def dategen():
    return datetime(2023, 5, randint(1, 10))


def update_report():
    totals = UrsipData.objects.values('date').annotate(
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
        res = to_model(row)
        res.date = dategen()
        res.save()



def to_model(row):
    res = UrsipData(
        company=row['company'],
        fact_qliq_data1=row['fact_qliq_data1'],
        fact_qliq_data2=row['fact_qliq_data2'],
        fact_qoil_data1=row['fact_qoil_data1'],
        fact_qoil_data2=row['fact_qoil_data2'],
        forecast_qliq_data1=row['forecast_qliq_data1'],
        forecast_qliq_data2=row['forecast_qliq_data2'],
        forecast_qoil_data1=row['forecast_qoil_data1'],
        forecast_qoil_data2=row['forecast_qoil_data2'],
    )
    return res
