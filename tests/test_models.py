import pytest
from django.core.exceptions import ValidationError

from economy_sector_module.models import EconomySector
from economy_sector_module.utils import STANDARDS


@pytest.mark.django_db
def test_create_economy_sector_raises_error():
    with pytest.raises(ValidationError):
        EconomySector.objects.create(
            level=1,
            label="Test",
            code="T1",
            parent=None,
            top_parent=None,
        )


@pytest.mark.django_db
def test_get_corresponding_code_returns_correct_record(initial_data):
    nace_level_1 = EconomySector.objects.get(code="A", standard=STANDARDS.nace)
    nace_level_2 = EconomySector.objects.get(code="01", standard=STANDARDS.nace)

    maped_ateco = EconomySector.objects.get(code="01", standard=STANDARDS.ateco)

    assert nace_level_2.get_corresponding_relation(standard=STANDARDS.ateco).to_sector == maped_ateco, \
        "Incorrect geography is returned!"

    assert nace_level_1.get_corresponding_relation(standard=STANDARDS.gics) is None, \
        "Incorrect geography is returned!"

