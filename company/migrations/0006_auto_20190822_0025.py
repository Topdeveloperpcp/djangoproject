# Generated by Django 2.1.11 on 2019-08-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Logo',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
