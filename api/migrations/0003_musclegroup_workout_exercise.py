# Generated by Django 4.0.4 on 2022-05-28 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='muscle_group_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('exercises', models.JSONField()),
                ('muscleGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_group', to='api.musclegroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('muscleGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_group', to='api.musclegroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
