from django.core.management.base import BaseCommand

from economy_sector_module.models import EconomySectorRelation
from economy_sector_module.utils import bulk_create_update_from_csv, get_csv_reader_from_remote

ECONOMY_SECTOR_RELATIONS_FILE_PATHS = [
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors_relations/nace_relations.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors_relations/ateco_relations.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors_relations/gics_relations.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors_relations/isic_relations.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors_relations/naics_relations.csv",

]


class Command(BaseCommand):
    help = 'Load relations between different economy sector into the database'

    def handle(self, **options):
        print("Started...")
        for remote_path in ECONOMY_SECTOR_RELATIONS_FILE_PATHS:
            print("Loading csv from remote...")
            reader = get_csv_reader_from_remote(remote_path)
            print("Preparing data to be created or updated...")
            bulk_create_update_from_csv(model=EconomySectorRelation, csv_reader=reader)
            print("Finished file...")
        print("Finished")
