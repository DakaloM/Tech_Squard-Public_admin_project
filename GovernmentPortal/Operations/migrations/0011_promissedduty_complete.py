# Generated by Django 4.1.2 on 2022-10-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0010_rename_promissed_duty_promissedduty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promissedduty',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
