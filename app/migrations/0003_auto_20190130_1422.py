# Generated by Django 2.1.5 on 2019-01-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190130_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
