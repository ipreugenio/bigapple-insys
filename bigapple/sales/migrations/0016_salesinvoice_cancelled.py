# Generated by Django 2.0.6 on 2018-07-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0015_auto_20180712_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesinvoice',
            name='cancelled',
            field=models.BooleanField(default=False, verbose_name='cancelled'),
        ),
    ]