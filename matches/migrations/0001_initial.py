# Generated by Django 3.0.8 on 2020-07-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('date', models.CharField(default='', max_length=1000)),
                ('status', models.CharField(default='', max_length=1000)),
                ('location', models.CharField(default='', max_length=1000)),
                ('teams', models.CharField(default='', max_length=20)),
                ('scores', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
