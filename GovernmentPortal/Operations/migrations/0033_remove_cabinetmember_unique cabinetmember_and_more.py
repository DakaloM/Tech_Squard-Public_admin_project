# Generated by Django 4.1.2 on 2022-10-30 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0032_cabinetmember_access_token_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='cabinetmember',
            name='unique cabinetmember',
        ),
        migrations.RemoveField(
            model_name='cabinetmember',
            name='access_token',
        ),
        migrations.AlterModelTable(
            name='cabinetmember',
            table=None,
        ),
    ]