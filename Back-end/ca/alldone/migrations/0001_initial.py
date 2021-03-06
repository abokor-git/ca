# Generated by Django 3.1.7 on 2021-03-26 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('ent_name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('is_client', models.BooleanField()),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('fourth_date', models.DateTimeField(blank=True, null=True)),
                ('about_me', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
