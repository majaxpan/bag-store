# Generated by Django 4.2.4 on 2023-08-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
