# Generated by Django 4.0.2 on 2022-06-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0021_alter_expenses_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
