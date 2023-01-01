# Generated by Django 4.1.4 on 2022-12-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_id', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('nin', 'National Identify Document'), ('voter', 'Voters Card'), ('driver', 'Drivers License')], max_length=30)),
                ('issued_on', models.DateField()),
                ('expired_on', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]