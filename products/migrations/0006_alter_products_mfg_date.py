# Generated by Django 4.1.4 on 2023-01-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='MFG_Date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]