# Generated by Django 2.1.3 on 2018-11-10 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20181106_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_student_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('subject', models.CharField(max_length=201)),
                ('batch', models.CharField(max_length=201)),
                ('date', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys')),
                ('student_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Students')),
            ],
        ),
        migrations.AlterField(
            model_name='semester_2',
            name='professer_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AlterField(
            model_name='semester_4',
            name='professer_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AlterField(
            model_name='semester_5',
            name='professer_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AlterField(
            model_name='semester_6',
            name='professer_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AlterField(
            model_name='semester_7',
            name='professer_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AlterField(
            model_name='semester_8',
            name='professer_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
    ]
