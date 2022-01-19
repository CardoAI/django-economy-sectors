import pytest as pytest
from django.core import management



@pytest.fixture
def initial_data():
    management.call_command('load_initial_data')
    management.call_command('load_relations_data')
