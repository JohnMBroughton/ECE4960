# Generated by Django 4.1.7 on 2023-02-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_lot_rfid_alter_lotsizes_num_spaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='RFID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lotsizes',
            name='num_spaces',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
