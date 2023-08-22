# Generated by Django 4.2.4 on 2023-08-22 08:03

import apps.cabinet_api.managers
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cabinet_api", "0003_alter_customuser_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", apps.cabinet_api.managers.CustomUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                max_length=150,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]