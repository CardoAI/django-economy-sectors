from django.core.exceptions import ObjectDoesNotExist
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
