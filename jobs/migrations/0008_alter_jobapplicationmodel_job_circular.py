# Generated by Django 5.0 on 2024-02-28 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20240228_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplicationmodel',
            name='job_circular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobcircularmodel'),
        ),
    ]
