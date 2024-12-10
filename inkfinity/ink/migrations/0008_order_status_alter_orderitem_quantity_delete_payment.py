# Generated by Django 5.1.3 on 2024-12-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0007_order_city_order_pincode_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
