# Generated by Django 4.1.2 on 2022-10-29 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0012_rename_head_officer_municipality_head_officer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operations.publicuser'),
        ),
    ]
