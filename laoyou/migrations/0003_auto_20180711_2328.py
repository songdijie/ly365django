# Generated by Django 2.0.4 on 2018-07-11 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laoyou', '0002_auto_20180711_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='forum',
            new_name='community',
        ),
    ]