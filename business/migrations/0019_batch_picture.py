# Generated by Django 4.0.2 on 2022-06-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0018_alter_batch_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='batch/'),
        ),
    ]
