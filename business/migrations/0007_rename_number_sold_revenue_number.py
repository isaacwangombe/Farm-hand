# Generated by Django 4.0.2 on 2022-06-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_rename_number_revenue_number_sold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenue',
            old_name='number_sold',
            new_name='number',
        ),
    ]
