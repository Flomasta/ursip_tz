from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR


class ReportHandler:
    def __init__(self, file_parser, save_report, update_result):
        self.file_parser = file_parser
        self.save_report = save_report
        self.update_result = update_result

    def get_data(self, path):
        file_path = os.path.join(BASE_DIR, path)
        data = self.file_parser(file_path)
        self.save_report(data)
