# Generated by Django 2.2.7 on 2019-12-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_port_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port_projects',
            name='port_date',
            field=models.DateField(),
        ),
    ]
