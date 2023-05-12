from django.core.management.base import BaseCommand, CommandError

from .report.report_handler import ReportHandler
from .report.file_parser import parse_file
from .report.save_to_db import save_report, update_report


class Command(BaseCommand):
    help = "Parse excel file"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, default=r'table_parser\data\table.xlsx',
                            help='Put the path from content root')

    def handle(self, *args, **options):
        file_path = options.get('path')
        report = ReportHandler(
            parse_file,
            save_report,
            update_report
        )
        report.create_report(file_path)
        print('success!')
