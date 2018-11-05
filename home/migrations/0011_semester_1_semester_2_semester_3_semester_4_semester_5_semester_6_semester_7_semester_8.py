# Generated by Django 2.1.3 on 2018-11-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
    ]