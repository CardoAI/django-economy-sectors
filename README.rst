============================
Django Economy Sector Module
============================

Quick start
-----------
1. Add "geographical_module" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'economy_sector_module',
    ]

2. Run ``python manage.py migrate`` to create the models.

3. Run ``python manage.py load_initial_data`` to populate the database with the initial records.

4. Run ``python manage.py load_relations_data`` to populate the database with the relationship between standards.
