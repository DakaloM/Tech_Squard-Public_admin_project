# Generated by Django 4.1.2 on 2022-10-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0022_alter_cabinetmember_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinetmember',
            name='access_token',
            field=models.CharField(auto_created=True, blank=True, max_length=50, null=True),
        ),
    ]