# Generated by Django 4.2.2 on 2023-06-22 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField()),
                ('link', models.URLField(max_length=150)),
                ('wrong', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('edge_case', models.TextField(blank=True, max_length=100, null=True)),
                ('solution', models.TextField(max_length=300)),
                ('option1', models.TextField(blank=True, max_length=300, null=True)),
                ('option2', models.TextField(blank=True, max_length=300, null=True)),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leetquizzer.difficulty')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leetquizzer.topic')),
            ],
        ),
    ]
