# Generated by Django 3.2.11 on 2022-02-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateField(),
        ),
    ]