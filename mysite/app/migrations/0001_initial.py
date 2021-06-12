# Generated by Django 3.1.6 on 2021-05-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=200)),
                ('testType', models.CharField(blank=True, max_length=200)),
                ('testAtime', models.CharField(blank=True, max_length=200)),
                ('question1', models.CharField(blank=True, max_length=200)),
                ('question2', models.CharField(blank=True, max_length=200)),
                ('question3', models.CharField(blank=True, max_length=200)),
                ('testBtime', models.CharField(blank=True, max_length=200)),
                ('question4', models.CharField(blank=True, max_length=200)),
                ('question5', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
