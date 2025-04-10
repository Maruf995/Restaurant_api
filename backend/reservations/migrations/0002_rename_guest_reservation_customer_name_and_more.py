# Generated by Django 4.2.20 on 2025-04-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='guest',
            new_name='customer_name',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
