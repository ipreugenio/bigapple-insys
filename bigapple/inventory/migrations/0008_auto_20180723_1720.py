# Generated by Django 2.0.6 on 2018-07-23 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgt', '0007_auto_20180718_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseRequisitionItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierSalesInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('vat', models.DecimalField(decimal_places=2, max_digits=50, verbose_name='vat')),
                ('total_amount', models.IntegerField(verbose_name='total_amount')),
            ],
        ),
        migrations.RemoveField(
            model_name='purchaserequisition',
            name='description',
        ),
        migrations.RemoveField(
            model_name='purchaserequisition',
            name='quantity',
        ),
        migrations.AddField(
            model_name='inventorycountasof',
            name='rm_type',
            field=models.CharField(blank=True, choices=[('--', '----------------'), ('LDPE', 'Low-density polyethylene'), ('LLDPE', 'Linear low-density polyethylene'), ('HDPE', 'High-density polyethylene'), ('PP', 'Polypropylene'), ('PET', 'Polyethylene terephthalate')], default='not specified', max_length=200, null=True, verbose_name='rm_type'),
        ),
        migrations.AddField(
            model_name='materialrequisition',
            name='status',
            field=models.CharField(default='waiting', max_length=200, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='status',
            field=models.CharField(default='waiting', max_length=200, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='materialrequisition',
            name='issued_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_mgt.Employee'),
        ),
        migrations.AlterField(
            model_name='supplierpo',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='total_amount'),
        ),
        migrations.AlterField(
            model_name='supplierpoitems',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=50, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='supplierpoitems',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=50, verbose_name='total_price'),
        ),
        migrations.AddField(
            model_name='suppliersalesinvoice',
            name='supplier_po',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.SupplierPO'),
        ),
        migrations.AddField(
            model_name='suppliersalesinvoice',
            name='supplier_po_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.SupplierPOItems'),
        ),
        migrations.AddField(
            model_name='purchaserequisitionitems',
            name='purchreq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.PurchaseRequisition'),
        ),
    ]