# Generated by Django 4.1.4 on 2023-01-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_profile_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_otp', models.IntegerField()),
            ],
        ),
    ]
