# Generated by Django 4.2.4 on 2023-08-24 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_product_chain_type_alter_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]