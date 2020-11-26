# Generated by Django 2.2.4 on 2020-11-26 10:23

import cms.models
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(help_text='Body of the banner')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(help_text='Body of the footer')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=255)),
                ('position', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permalink', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('imports', models.TextField(blank=True, help_text='External imports like css,js files, will be placed in <head> tag (already includes bootstrap4 and jQuery)', null=True)),
                ('content', models.TextField(help_text='Body of the page')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaticFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=70, unique=True, validators=[cms.models.validate_filename])),
                ('file', models.FileField(help_text='Please upload static file (image, css, js, etc). This file will be accessible at static/cms/filename', storage=django.core.files.storage.FileSystemStorage(base_url='/', location='cms'), upload_to=cms.models.get_filename)),
            ],
        ),
        migrations.CreateModel(
            name='SubNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=255)),
                ('position', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('nav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Nav')),
            ],
        ),
    ]