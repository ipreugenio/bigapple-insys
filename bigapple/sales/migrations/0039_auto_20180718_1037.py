# Generated by Django 2.0.6 on 2018-07-18 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0038_auto_20180718_1029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductionCosts',
            new_name='ProductionCost',
        ),
        migrations.AlterField(
            model_name='clientitem',
            name='color_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='color_quantity'),
        ),
    ]
