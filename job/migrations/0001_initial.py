# Generated by Django 4.2.14 on 2024-08-01 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('published_at', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.category')),
            ],
        ),
    ]