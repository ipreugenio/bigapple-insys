# Generated by Django 2.0.6 on 2018-07-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgt', '0003_auto_20180703_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequisition',
            name='date_issued',
            field=models.DateField(blank=True, verbose_name='date_issued'),
        ),
    ]
