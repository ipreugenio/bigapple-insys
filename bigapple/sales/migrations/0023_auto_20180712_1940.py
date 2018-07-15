# Generated by Django 2.0.6 on 2018-07-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0022_auto_20180712_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Cancelled', 'Cancelled')], default='Open', max_length=200, verbose_name='status'),
        ),
    ]