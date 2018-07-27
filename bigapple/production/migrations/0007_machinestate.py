# Generated by Django 2.0.6 on 2018-07-23 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production_mgt', '0006_auto_20180723_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0, verbose_name='state')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production_mgt.Machine')),
            ],
        ),
    ]