# Generated by Django 2.0.2 on 2018-02-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='study_date',
            field=models.DateField(blank=True, null=True, verbose_name='Study Date'),
        ),
    ]
