from django.core.management.base import BaseCommand
from django.core.management import call_command

fixtures = [
    "initial_data/nace_standard.yaml",
    "initial_data/ateco_standard.yaml",
    "initial_data/gics_standard.yaml",
    "initial_data/isic_standard.yaml",
    "sae_standard.yaml",
]


class Command(BaseCommand):
    help = 'Load economy sector data from fixtures into the database'

    def handle(self, **options):
        for fixture in fixtures:
            print(f"Loading fixture {fixture}")
            call_command("loaddata", fixture)
