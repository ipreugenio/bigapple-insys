# Generated by Django 2.0.6 on 2018-07-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0029_auto_20180714_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesinvoice',
            name='total_amount_computed',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, verbose_name='total_amount_computed'),
            preserve_default=False,
        ),
    ]
