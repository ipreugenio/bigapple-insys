# Generated by Django 2.0.6 on 2018-06-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0005_auto_20180628_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientpo',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='clientpo',
            name='status',
            field=models.CharField(choices=[('w', 'waiting'), ('a', 'approved'), ('u', 'under production'), ('r', 'ready for delivery'), ('d', 'disapproved')], default='waiting', max_length=200, verbose_name='status'),
        ),
    ]
