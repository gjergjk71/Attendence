# Generated by Django 2.1.3 on 2018-11-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20181104_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultys',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]