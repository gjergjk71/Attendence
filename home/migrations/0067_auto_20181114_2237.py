# Generated by Django 2.1.3 on 2018-11-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_auto_20181114_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_student_attendance',
            name='student_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Students'),
        ),
    ]
