# Generated by Django 4.2.5 on 2024-02-08 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contant',
            new_name='content',
        ),
    ]
