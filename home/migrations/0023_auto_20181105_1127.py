# Generated by Django 2.1.3 on 2018-11-05 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20181104_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester_1',
            name='professerr_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Sections'),
        ),
    ]