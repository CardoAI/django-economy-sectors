from django.core.management.base import BaseCommand
from django.db import transaction

from economy_sectors.models import EconomySectorRelation
from economy_sectors.utils import bulk_create_update_from_csv, get_csv_reader_from_remote


class Command(BaseCommand):
    help = 'Load relations between different economy sector into the database'

    # add database argument
    def add_arguments(self, parser):
        parser.add_argument('--database', action='store', dest='database', default='default',
                            help='Specify the database to load the data to. Defaults to "default"')

    def handle(self, **options):
        database = options['database']
        self.stdout.write("Please insert the signed URLs and hit enter. Once done inserting just hit enter with no input.")
        urls_list = []
        while True:
            u_input = input('URL:')
            if u_input:
                urls_list.append(u_input)
            else:
                for i, url in enumerate(urls_list):
                    self.stdout.write(f'{i}-{url}\n')
                confirm = input('Confirm that the URLs entered are correct by pressing Y. '
                                'If not press N and reinsert the URLs.'
                                ' If you want to quit the command pres Q or another char.')
                if confirm.lower() == 'y':
                    with transaction.atomic(using=database):
                        for filename in urls_list:
                            self.stdout.write(f"Processing {filename.split('?')[0].split('/')[-1]}...")
                            self.stdout.write("Loading csv from remote...")
                            reader = get_csv_reader_from_remote(f"{filename}")
                            self.stdout.write("Preparing data to be created or updated...")
                            bulk_create_update_from_csv(model=EconomySectorRelation, csv_reader=reader)
                            self.stdout.write("Finished file.\n")
                        self.stdout.write("Finished all files.")
                        return

                elif confirm.lower() == 'n':
                    urls_list = []
                else:
                    self.stdout.write('Exiting...')
                    return
