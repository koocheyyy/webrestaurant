# Generated by Django 4.0.3 on 2024-02-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_place_tax_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
