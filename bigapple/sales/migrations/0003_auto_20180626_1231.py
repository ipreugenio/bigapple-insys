# Generated by Django 2.0.6 on 2018-06-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0002_remove_clientpo_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientitem',
            name='laminate',
            field=models.BooleanField(verbose_name='laminate'),
        ),
    ]
