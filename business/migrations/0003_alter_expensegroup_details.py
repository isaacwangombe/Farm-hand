# Generated by Django 4.0.2 on 2022-06-19 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_expensegroup_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensegroup',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='business.expensedetails'),
        ),
    ]