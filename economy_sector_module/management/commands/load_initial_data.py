from django.core.management.base import BaseCommand
from django.core.management import call_command

fixtures = [
    "nace_standard.yaml",
    "ateco_standard.yaml",
    "gics_standard.yaml",
    "isic_standard.yaml",
    "sic_standard.yaml",
]


class Command(BaseCommand):
    help = 'Load economy sector data from fixtures into the database'

    def handle(self, **options):
        for fixture in fixtures:
            print(f"Loading fixture {fixture}")
            call_command("loaddata", fixture)
