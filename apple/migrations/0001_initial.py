# Generated by Django 2.2.6 on 2019-11-09 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branches',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_city', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='bikes',
            fields=[
                ('bike_id', models.AutoField(primary_key=True, serialize=False)),
                ('bike_company', models.CharField(max_length=50)),
                ('bike_model', models.CharField(max_length=100)),
                ('bike_cost', models.IntegerField()),
                ('bike_availability', models.IntegerField(default=1)),
                ('bike_colour', models.CharField(max_length=30)),
                ('bike_millage', models.IntegerField()),
                ('bike_cc', models.IntegerField(default=0)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apple.branches')),
            ],
        ),
    ]