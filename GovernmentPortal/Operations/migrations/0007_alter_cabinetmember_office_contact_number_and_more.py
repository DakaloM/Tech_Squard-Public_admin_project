# Generated by Django 4.1.2 on 2022-10-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0006_remove_publicsector_head_minister_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinetmember',
            name='office_contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
