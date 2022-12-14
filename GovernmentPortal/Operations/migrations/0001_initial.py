# Generated by Django 4.1.2 on 2022-10-29 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=225)),
                ('role', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('office_contact_number', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('email', models.EmailField(max_length=225)),
                ('emplyment_status', models.CharField(choices=[('Unemplyed', 'Unemplyed'), ('Employed', 'Employed')], max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='PublicSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('year_budget', models.CharField(blank=True, max_length=100, null=True)),
                ('head_minister', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Operations.cabinetmember')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=20)),
                ('project_manager', models.CharField(max_length=255)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operations.publicsector')),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=100)),
                ('Head_officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('political_party', models.CharField(max_length=200)),
                ('year_budget', models.CharField(max_length=100, null=True)),
                ('Municipality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Operations.municipality')),
            ],
        ),
    ]
