# Generated by Django 4.1.7 on 2023-02-21 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_lotsizes_rename_parkingspace_c02'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='C02',
            new_name='Lot',
        ),
    ]
