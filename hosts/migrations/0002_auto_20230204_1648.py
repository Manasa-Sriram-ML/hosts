# Generated by Django 3.2.17 on 2023-02-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosts',
            name='disk_capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hosts',
            name='mem_in_gb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hosts',
            name='num_cpus',
            field=models.IntegerField(default=0),
        ),
    ]
