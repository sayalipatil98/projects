# Generated by Django 4.1.1 on 2022-09-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('booknm', models.CharField(max_length=100)),
                ('bookpublisher', models.CharField(max_length=100)),
                ('bookpr', models.IntegerField()),
            ],
        ),
    ]
