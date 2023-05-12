from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR


class ReportHandler:
    def __init__(self, read_excel, save_report, update_report):
        self.load_data = read_excel
        self.save_report = save_report
        self.update_report = update_report

    def create_report(self, path):
        file_path = os.path.join(BASE_DIR, path)
        data = self.load_data(file_path)
        self.save_report(data)
        self.update_report()
