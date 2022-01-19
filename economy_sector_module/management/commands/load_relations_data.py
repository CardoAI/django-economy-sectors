from django.core.management.base import BaseCommand
from django.core.management import call_command

fixtures = [
    "standards_relations/nace_relations.yaml",
    "standards_relations/ateco_relations.yaml",
    "standards_relations/gics_relations.yaml",
    "standards_relations/isic_relations.yaml",
]


class Command(BaseCommand):
    help = 'Load relations between different economy sector from fixtures into the database'

    def handle(self, **options):
        for fixture in fixtures:
            print(f"Loading fixture {fixture}")
            call_command("loaddata", fixture)
