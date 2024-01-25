# Generated by Django 2.2.7 on 2019-11-22 18:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apple', '0003_bikes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('take_time', models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 43, 51, 911999))),
                ('give_time', models.DateTimeField(default=datetime.datetime(2019, 11, 22, 23, 43, 51, 911999))),
                ('bike_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apple.bikes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]