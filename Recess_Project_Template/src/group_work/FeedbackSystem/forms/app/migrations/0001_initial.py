# Generated by Django 4.2.4 on 2023-08-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampusFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=1)),
                ('q2', models.CharField(max_length=1)),
                ('q3', models.CharField(max_length=1)),
                ('q4', models.CharField(max_length=1)),
                ('q5', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=1)),
                ('q2', models.CharField(max_length=1)),
                ('q3', models.CharField(max_length=1)),
                ('q4', models.CharField(max_length=1)),
                ('q5', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='InstructorFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=1)),
                ('q2', models.CharField(max_length=1)),
                ('q3', models.CharField(max_length=1)),
                ('q4', models.CharField(max_length=1)),
                ('q5', models.CharField(max_length=1)),
            ],
        ),
    ]
