# Generated by Django 4.1.7 on 2023-03-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LotSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_spaces', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RFID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lot', models.CharField(max_length=200)),
                ('RFID', models.IntegerField(default=0)),
            ],
        ),
    ]
