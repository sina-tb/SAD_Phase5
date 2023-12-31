# Generated by Django 4.2.3 on 2023-07-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=512)),
                ('last_name', models.CharField(max_length=512)),
                ('type', models.CharField(choices=[('1', 'Supporter'), ('0', 'Patient')], default='0', max_length=2)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive')], default='IN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.package')),
                ('supporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_supporter', to='healthcare.userprofile')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_userprofile', to='healthcare.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PrerequisitesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.package')),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=100)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.record')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.prerequisitestype')),
            ],
        ),
    ]
