# Generated by Django 4.2.14 on 2024-08-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_rename_benefits_job_benefits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='benefits',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='job',
            name='qualifications',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsibility',
            field=models.TextField(max_length=10000),
        ),
    ]