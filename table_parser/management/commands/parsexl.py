from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = "Parse excel file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Successfully parsed')
        )
