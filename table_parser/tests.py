import openpyxl
import pandas as pd
from django.test import TestCase
from table_parser.management.commands.parsexl import ReportHandler
from table_parser.management.commands.report.file_parser import parse_file
from table_parser.management.commands.report.save_to_db import save_report, update_report

from table_parser.models import UrsipData


# Create your tests here.
class UrsipTestCase(TestCase):
    def test_smoke(self):
        report = ReportHandler(
            parse_file,
            save_report,
            update_report
        )
        report.create_report(r'table_parser/data/table.xlsx')
        assert UrsipData.objects.all().count() == 20
        assert UrsipData.objects.get(id=1).company == 'company1'
        assert UrsipData.objects.get(id=5).forecast_qliq_data2 == 26

    def test_parse_file_smoke(self):
        parse_file(r'table_parser/data/table.xlsx')

    def test_parse_file_one_row(self):
        df_actual = parse_file(r'table_parser/data/table_one_row.xlsx').to_dict(orient='list')
        df_expected = {
            'company': ['company1'],
            'fact_qliq_data1': [10],
            'fact_qliq_data2': [20],
            'fact_qoil_data1': [30],
            'fact_qoil_data2': [40],
            'forecast_qliq_data1': [12],
            'forecast_qliq_data2': [22],
            'forecast_qoil_data1': [15],
            'forecast_qoil_data2': [25]
        }
        assert df_actual == df_expected

    def test_save_data(self):
        save_report(parse_file(r'table_parser/data/table_one_row.xlsx'))
