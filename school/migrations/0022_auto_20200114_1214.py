# Generated by Django 2.2 on 2020-01-14 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_teacher_teacher_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_class',
            field=models.ForeignKey(default='No_class', null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Class'),
        ),
    ]
