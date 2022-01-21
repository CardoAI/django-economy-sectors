============================
Django Economy Sector Module
============================

Quick start
-----------
1. Add "geographical_module" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'economy_sectors',
    ]

2. Run ``python manage.py migrate`` to create the models.

3. Run ``python manage.py load_standards_data`` to populate the database with the initial records.

4. Run ``python manage.py load_standards_relations`` to populate the database with the relationship between standards.
