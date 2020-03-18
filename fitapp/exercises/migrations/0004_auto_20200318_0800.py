# Generated by Django 3.0.1 on 2020-03-18 12:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_movementstep_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='instruction',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='exercise',
            name='instructions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=255), default=[], size=None),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises', models.ManyToManyField(to='exercises.Exercise')),
            ],
        ),
    ]
