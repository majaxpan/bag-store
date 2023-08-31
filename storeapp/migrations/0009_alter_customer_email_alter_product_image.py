# Generated by Django 4.2.4 on 2023-08-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0008_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=2083, null=True),
        ),
    ]
