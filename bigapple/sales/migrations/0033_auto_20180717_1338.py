# Generated by Django 2.0.6 on 2018-07-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0032_auto_20180715_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientitem',
            name='thickness',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12, verbose_name='thickness'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='constant',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='constant'),
        ),
    ]