import csv
import io
from urllib.error import HTTPError
from urllib.request import urlopen

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import QuerySet
from model_utils import Choices

STANDARDS = Choices(
    (0, "unspecified", "Unspecified"),
    (1, "nace", "NACE"),
    (2, "ateco", "ATECO"),
    (3, "gics", "GICS"),
    (4, "isic", "ISIC"),  # rev4
    (5, "naics", "NAICS"),  # 2022
    (6, "sic", "SIC"),
    (7, "sae", "SAE"),
)


def get_or_none(queryset: QuerySet, *args, **kwargs):
    try:
        return queryset.get(*args, **kwargs)
    except ObjectDoesNotExist:
        return None


def get_csv_reader_from_remote(remote_path: str):
    """
    Read a csv file from a remote server and return a DictReader object
    """
    try:
        with urlopen(remote_path) as file:
            mycsv = io.StringIO(file.read().decode())
            return csv.DictReader(mycsv)
    except HTTPError:
        pass


@transaction.atomic()
def bulk_create_update_from_csv(model, csv_reader: csv.DictReader, batch_size=500):
    """
    Function that creates 2 lists holding the objects that need to be created and the ones which
    need to be updated while reading lines from a DictReader object.
    """
    obj_to_be_created = []
    obj_to_be_updated = []
    _ids = set(model.objects.values_list('id', flat=True))
    for row in csv_reader:
        if int(row['id']) in _ids:
            obj_to_be_updated.append(model(**row))
        else:
            obj_to_be_created.append(model(**row))

    csv_reader.fieldnames.remove('id')
    model.objects.bulk_update(obj_to_be_updated, fields=csv_reader.fieldnames,
                              batch_size=batch_size)
    model.objects.bulk_create(obj_to_be_created, batch_size=batch_size)
