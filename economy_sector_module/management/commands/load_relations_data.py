from django.core.management.base import BaseCommand
from django.core.management import call_command

fixtures = [
    "nace_relations.yaml",
    "ateco_relations.yaml",
    "gics_relations.yaml",
    "isic_relations.yaml",
    "naics_relations.yaml",
]


class Command(BaseCommand):
    help = 'Load relations between different economy sector from fixtures into the database'

    def handle(self, **options):
        for fixture in fixtures:
            print(f"Loading fixture {fixture}")
            call_command("loaddata", fixture)
