# Generated by Django 5.0.2 on 2024-03-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_parcel_deliveryproof'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryproof',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
