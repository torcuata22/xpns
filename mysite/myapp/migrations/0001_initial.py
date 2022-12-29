# Generated by Django 4.1.4 on 2022-12-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]