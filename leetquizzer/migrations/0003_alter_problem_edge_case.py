# Generated by Django 4.2.2 on 2023-07-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leetquizzer', '0002_alter_problem_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='edge_case',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
