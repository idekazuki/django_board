# Generated by Django 2.0.2 on 2020-07-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0009_boardmodel_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
