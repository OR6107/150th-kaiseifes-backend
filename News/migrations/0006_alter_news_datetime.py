# Generated by Django 3.2.4 on 2021-06-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_auto_20210629_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='datetime',
            field=models.DateField(auto_now=True),
        ),
    ]
