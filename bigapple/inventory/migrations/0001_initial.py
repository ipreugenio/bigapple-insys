# Generated by Django 2.1a1 on 2018-06-25 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts_mgt', '0001_initial'),
        ('sales_mgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentRMinProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rm_name', models.CharField(default='not specified', max_length=200, verbose_name='rm_name')),
                ('rm_type', models.CharField(choices=[('LDPE', 'Low-density polyethylene'), ('LLDPE', 'Linear low-density polyethylene'), ('HDPE', 'High-density polyethylene'), ('PP', 'Polypropylene'), ('PET', 'Polyethylene terephthalate')], default='not specified', max_length=200, verbose_name='rm_type')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryCountAsof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_count', models.IntegerField(default=0, verbose_name='new_count')),
                ('date_counted', models.DateField(verbose_name='date_counted')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialRequisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='date_issued')),
                ('issued_to', models.CharField(max_length=200, verbose_name='issued_to')),
                ('brand', models.CharField(max_length=200, verbose_name='brand')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('to_be_used_for', models.CharField(max_length=200, verbose_name='to_be_used_for')),
                ('shift', models.CharField(choices=[('1', 'shift 1'), ('2', 'shift 2'), ('3', 'shift 3')], default='not specified', max_length=200, verbose_name='shift')),
                ('approval', models.BooleanField(default=False, verbose_name='approval')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRequisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='date_issued')),
                ('date_required', models.DateField(verbose_name='date_required')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('approval', models.BooleanField(default=False, verbose_name='approval')),
                ('placed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_mgt.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, verbose_name='item_name')),
                ('item_type', models.CharField(choices=[('RM', 'Raw Materials'), ('MP', 'Machine Parts'), ('INK', 'Ink')], default='not specified', max_length=200, verbose_name='item_type')),
                ('price', models.IntegerField(verbose_name='price')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_mgt.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierPO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('delivery_date', models.DateField(verbose_name='delivery_date')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_mgt.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierPOTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retrieved', models.BooleanField(default=False, verbose_name='retrieved')),
                ('date_retrieved', models.DateField(blank=True, default='not yet retrieved', verbose_name='date_retrieved')),
                ('supplier_po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.SupplierPO')),
            ],
        ),
        migrations.AddField(
            model_name='currentrminproduction',
            name='raw_material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.Inventory'),
        ),
    ]
