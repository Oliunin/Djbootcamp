# Generated by Django 2.2.6 on 2019-10-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=264)),
                ('u_lastname', models.CharField(max_length=264)),
                ('u_email', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]