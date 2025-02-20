# Generated by Django 5.1.5 on 2025-01-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('amount', models.IntegerField()),
                ('validity', models.CharField(max_length=11)),
                ('value', models.CharField(max_length=10)),
            ],
        ),
    ]
