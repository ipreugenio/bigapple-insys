# Generated by Django 2.0.6 on 2018-07-23 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production_mgt', '0014_machineschedule_workerschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineschedule',
            name='client_po',
        ),
        migrations.RemoveField(
            model_name='machineschedule',
            name='machine',
        ),
        migrations.RemoveField(
            model_name='workerschedule',
            name='machine',
        ),
        migrations.RemoveField(
            model_name='workerschedule',
            name='worker',
        ),
        migrations.DeleteModel(
            name='MachineSchedule',
        ),
        migrations.DeleteModel(
            name='WorkerSchedule',
        ),
    ]
