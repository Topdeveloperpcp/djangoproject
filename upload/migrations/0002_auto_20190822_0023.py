# Generated by Django 2.1.11 on 2019-08-21 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='image',
            new_name='Logo',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='content',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='title',
        ),
    ]
