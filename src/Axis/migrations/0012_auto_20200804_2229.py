# Generated by Django 3.0.8 on 2020-08-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Axis', '0011_auto_20200804_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Payment Confirmed, Processing Order', 'Payment Confirmed, Processing Order'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]