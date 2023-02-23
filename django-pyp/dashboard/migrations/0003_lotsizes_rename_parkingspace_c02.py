# Generated by Django 4.1.7 on 2023-02-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_parkingspace_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_spaces', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='ParkingSpace',
            new_name='C02',
        ),
    ]
