# Generated by Django 5.0 on 2024-02-27 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_jobapplicationmodel_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplicationmodel',
            name='applied_at',
        ),
        migrations.RemoveField(
            model_name='jobapplicationmodel',
            name='coverletter',
        ),
        migrations.RemoveField(
            model_name='jobapplicationmodel',
            name='skills',
        ),
    ]