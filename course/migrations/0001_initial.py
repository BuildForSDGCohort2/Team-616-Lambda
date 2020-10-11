# Generated by Django 2.2 on 2019-12-22 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('cover_picture', imagekit.models.fields.ProcessedImageField(default='default.png', upload_to='course/images')),
                ('course_description', models.TextField()),
                ('course_price', models.IntegerField()),
                ('rreleased_on', models.DateField(auto_now=True)),
                ('authur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
                ('video_description', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('course', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now=True)),
                ('course_files', models.FileField(blank=True, max_length=250, null=True, upload_to='course/course_files')),
                ('text', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.CourseVideo')),
            ],
        ),
    ]