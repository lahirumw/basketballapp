# Generated by Django 3.0.8 on 2020-07-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('year', models.CharField(default='', max_length=1000)),
                ('teams', models.CharField(default='', max_length=1000)),
                ('trophy', models.CharField(default='', max_length=1000)),
                ('Country', models.CharField(default='', max_length=20)),
                ('winner', models.CharField(default='', max_length=1000)),
                ('runnerUp', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
