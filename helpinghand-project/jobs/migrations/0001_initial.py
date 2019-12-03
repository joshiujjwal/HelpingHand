# Generated by Django 2.2.7 on 2019-12-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200)),
                ('job_description', models.TextField(default='')),
                ('job_type', models.TextField(blank=True, default='')),
                ('skills_needed', models.CharField(blank=True, default='', max_length=100)),
                ('hourly_pay', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
