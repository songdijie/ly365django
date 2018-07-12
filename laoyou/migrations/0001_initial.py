# Generated by Django 2.0.4 on 2018-07-12 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('body', models.TextField(max_length=4194304)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('viewcount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('member', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CityCommunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communitys', to='laoyou.City')),
            ],
        ),
        migrations.CreateModel(
            name='CityCommunityNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='laoyou.CityCommunity')),
            ],
        ),
        migrations.CreateModel(
            name='CityCommunityNewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('vote', models.PositiveIntegerField(default=0)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='laoyou.CityCommunityNews')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=100)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laoyou.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('member', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('member', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laoyou.Community')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='laoyou.Topic'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
