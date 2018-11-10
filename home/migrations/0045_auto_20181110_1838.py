# Generated by Django 2.1.3 on 2018-11-10 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20181110_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_student_attendance',
            name='attend',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='add_student_attendance',
            name='student_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Students'),
        ),
    ]