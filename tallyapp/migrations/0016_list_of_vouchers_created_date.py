# Generated by Django 4.0.6 on 2022-07-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0015_accounting_voucher_creation_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_of_vouchers_created',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
