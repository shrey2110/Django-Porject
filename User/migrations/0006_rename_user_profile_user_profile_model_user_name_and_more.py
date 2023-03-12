# Generated by Django 4.1.4 on 2023-01-28 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0005_otp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='User_profile_model',
        ),
        migrations.CreateModel(
            name='user_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='user_profile_model',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='User.user_name'),
        ),
    ]
