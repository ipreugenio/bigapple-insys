# Generated by Django 2.0.6 on 2018-07-14 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0027_auto_20180714_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpayment',
            name='credit_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales_mgt.ClientCreditStatus'),
        ),
        migrations.AlterField(
            model_name='clientpayment',
            name='invoice_issued',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales_mgt.SalesInvoice'),
        ),
    ]
