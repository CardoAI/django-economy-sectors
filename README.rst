======================
Django Economy Sectors
======================

This library allows the utilization of Economy Sectors, from different standards,
as well as conversion between them.

Supported standards:

* NACE
* ATECO
* GICS
* ISIC (rev4)
* NAICS (2022)
* SIC
* SAE

Quick start
-----------
1. Add "economy_sectors" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'economy_sectors',
    ]

2. Run ``python manage.py migrate`` to create the models.

3. Run ``python manage.py load_standards_data`` to populate the database with the initial records.

4. Run ``python manage.py load_standards_relations`` to populate the database with the relationship between standards.
