# Generated by Django 4.1.4 on 2023-01-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
