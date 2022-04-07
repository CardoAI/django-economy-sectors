import pytest
from model_bakery import baker

from economy_sectors.models import EconomySector, EconomySectorRelation
from economy_sectors.models.economy_sector import Standard


@pytest.mark.django_db
def test_get_corresponding_sector_returns_correct_record():
    nace_standard = Standard.objects.create(name='NACE')
    ateco_standard = Standard.objects.create(name="ATECO")
    nace_sector: EconomySector = baker.make('EconomySector', standard=nace_standard)
    ateco_sector: EconomySector = baker.make('EconomySector', standard=ateco_standard)

    EconomySectorRelation.objects.create(
        from_sector=nace_sector,
        to_standard=ateco_standard,
        to_sector=ateco_sector
    )

    assert nace_sector.get_corresponding_sector(to_standard=ateco_standard) == ateco_sector, \
        "Incorrect economy sector is returned!"


@pytest.mark.django_db
def test_get_corresponding_sector_returns_none_when_relation_not_exists():
    nace_standard = Standard.objects.create(name='NACE')
    gics_standard = Standard.objects.create(name='GICS')
    sector: EconomySector = baker.make('EconomySector', standard=nace_standard)

    assert sector.get_corresponding_sector(to_standard=gics_standard) is None, \
        "Corresponding sector is returned, but relation does not exist!"
