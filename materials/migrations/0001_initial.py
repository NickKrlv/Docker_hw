# Generated by Django 5.0.2 on 2024-02-27 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='course_name')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='preview')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='course_name')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='preview')),
                ('description', models.TextField(verbose_name='description')),
                ('url', models.CharField(blank=True, null=True, verbose_name='url')),
                ('course_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='materials.course', verbose_name='course_id')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]