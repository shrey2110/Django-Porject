# Generated by Django 4.1.4 on 2023-01-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_profile_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_profile_pic',
            field=models.ImageField(default='/profile_pic/avatar_2x.png', null=True, upload_to='user_p'),
        ),
    ]
