# Generated by Django 4.1.4 on 2023-01-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_rename_user_profile_user_profile_model_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile_model',
            name='user_gender',
            field=models.CharField(choices=[('', 'Gender'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10),
        ),
    ]