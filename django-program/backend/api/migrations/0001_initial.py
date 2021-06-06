# Generated by Django 3.2.4 on 2021-06-06 14:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('solution1', models.TextField(default='none')),
                ('solution2', models.TextField(default='none')),
                ('postedby', models.CharField(default='admin', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('author', models.CharField(default='joel wembo', max_length=100)),
                ('username', models.CharField(default='joelwembo', max_length=100)),
                ('link', models.CharField(default='https:google.com', max_length=100)),
                ('date_field', models.DateField(default=django.utils.timezone.now, max_length=150)),
            ],
        ),
    ]
