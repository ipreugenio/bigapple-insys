# Generated by Django 2.0.6 on 2018-07-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0040_auto_20180718_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientitem',
            name='thickness',
            field=models.DecimalField(decimal_places=3, max_digits=12, verbose_name='thickness'),
        ),
    ]
