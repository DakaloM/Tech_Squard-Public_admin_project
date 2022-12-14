# Generated by Django 4.1.2 on 2022-10-29 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0004_remove_cabinetmember_email_remove_publicuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='publicsector',
            name='head_minister',
        ),
        migrations.AlterField(
            model_name='cabinetmember',
            name='role',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operations.cabinetposition'),
        ),
        migrations.AddField(
            model_name='publicsector',
            name='head_minister',
            field=models.ManyToManyField(null=True, to='Operations.cabinetmember'),
        ),
    ]
