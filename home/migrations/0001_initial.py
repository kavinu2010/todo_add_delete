# Generated by Django 5.1.4 on 2024-12-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddTask', models.CharField(max_length=30)),
                ('time', models.TimeField()),
            ],
        ),
    ]
