# Generated by Django 4.2.20 on 2025-04-11 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_project_options_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
