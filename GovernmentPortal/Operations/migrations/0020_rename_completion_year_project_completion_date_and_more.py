# Generated by Django 4.1.2 on 2022-10-30 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0019_project_completion_year_project_starting_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='completion_year',
            new_name='completion_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='starting_year',
            new_name='starting_date',
        ),
    ]
