import pytest
from model_bakery import baker

from economy_sectors.models import EconomySector, EconomySectorRelation
from economy_sectors.utils import STANDARDS


@pytest.mark.django_db
def test_get_corresponding_sector_returns_correct_record():
    nace_sector: EconomySector = baker.make('EconomySector', standard=STANDARDS.nace)
    ateco_sector: EconomySector = baker.make('EconomySector', standard=STANDARDS.ateco)

    EconomySectorRelation.objects.create(
        from_sector=nace_sector,
        to_standard=STANDARDS.ateco,
        to_sector=ateco_sector
    )

    assert nace_sector.get_corresponding_sector(to_standard=STANDARDS.ateco) == ateco_sector, \
        "Incorrect economy sector is returned!"


@pytest.mark.django_db
def test_get_corresponding_sector_returns_none_when_relation_not_exists():
    sector: EconomySector = baker.make('EconomySector', standard=STANDARDS.nace)

    assert sector.get_corresponding_sector(to_standard=STANDARDS.gics) is None, \
        "Corresponding sector is returned, but relation does not exist!"
