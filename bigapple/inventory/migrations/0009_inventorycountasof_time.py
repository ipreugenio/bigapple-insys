# Generated by Django 2.0.6 on 2018-07-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgt', '0008_auto_20180723_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorycountasof',
            name='time',
            field=models.TimeField(auto_now_add=True, default=1, verbose_name='time'),
            preserve_default=False,
        ),
    ]
