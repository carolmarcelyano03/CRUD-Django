# Generated by Django 4.1.7 on 2023-02-23 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eaddress', models.CharField(max_length=100)),
                ('ektpid', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pict', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'picture',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exid', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('information', models.CharField(max_length=255)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'experience',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edid', models.CharField(max_length=20)),
                ('edschoolname', models.CharField(max_length=100)),
                ('edmajor', models.CharField(max_length=50)),
                ('edyearentry', models.DateField()),
                ('edyeargraduation', models.DateField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'education',
            },
        ),
    ]