# Generated by Django 2.2 on 2019-12-19 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20191219_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
