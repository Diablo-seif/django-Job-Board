# Generated by Django 4.2.14 on 2024-08-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='job/photo/%m/%d'),
            preserve_default=False,
        ),
    ]
