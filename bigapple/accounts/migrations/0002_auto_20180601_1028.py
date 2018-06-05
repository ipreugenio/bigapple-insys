# Generated by Django 2.0.5 on 2018-06-01 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_mgt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='middle_initial',
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(default='not_specified', max_length=200, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='not_specified', max_length=200, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='pagibig',
            field=models.CharField(blank=True, max_length=200, verbose_name='pagibig'),
        ),
        migrations.AddField(
            model_name='employee',
            name='philhealth',
            field=models.CharField(blank=True, max_length=200, verbose_name='philhealth'),
        ),
        migrations.AddField(
            model_name='employee',
            name='sss',
            field=models.CharField(blank=True, max_length=200, verbose_name='sss'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tin',
            field=models.CharField(blank=True, max_length=200, verbose_name='tin'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='accounts',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_mgt.Account'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('GM', 'General Manager'), ('SC', 'Sales Coordinator'), ('SA', 'Sales Agent'), ('CC', 'Credits and Collection'), ('SV', 'Supervisor'), ('LL', 'Line Leader'), ('PM', 'Production Manager'), ('C', 'Cutting'), ('P', 'Printing'), ('E', 'Extruder'), ('D', 'Delivery'), ('W', 'Warehouse'), ('U', 'Utility'), ('M', 'Maintenance')], default='not specified', max_length=200, verbose_name='position'),
        ),
    ]