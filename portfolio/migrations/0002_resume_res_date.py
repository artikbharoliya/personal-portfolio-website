# Generated by Django 2.2.6 on 2019-12-18 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='res_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
