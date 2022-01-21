from django.core.management.base import BaseCommand

from economy_sector_module.models import EconomySector
from economy_sector_module.utils import get_csv_reader_from_remote, bulk_create_update_from_csv

ECONOMY_SECTOR_FILE_PATHS = [
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/nace_standard.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/ateco_standard.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/gics_standard.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/isic_standard.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/sic_standard.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/sae_standard.csv",
    "https://package-files.s3.eu-central-1.amazonaws.com/django-economy-sectors/economy_sectors/naics_standard.csv",
]


class Command(BaseCommand):
    help = 'Load economy sector data into the database'

    def handle(self, **options):
        print("Started...")
        for remote_path in ECONOMY_SECTOR_FILE_PATHS:
            print("Loading csv from remote...")
            reader = get_csv_reader_from_remote(remote_path)
            print("Preparing data to be created or updated...")
            bulk_create_update_from_csv(model=EconomySector, csv_reader=reader)
            print("Finished file...")
        print("Finished")
