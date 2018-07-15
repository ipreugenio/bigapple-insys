# Generated by Django 2.0.6 on 2018-07-12 05:15

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0012_auto_20180712_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcreditstatus',
            name='outstanding_balance',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12, verbose_name='outstanding_balance'),
        ),
    ]