# Generated by Django 3.2.8 on 2022-06-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dishName',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='dishName',
            field=models.CharField(max_length=512),
        ),
    ]
