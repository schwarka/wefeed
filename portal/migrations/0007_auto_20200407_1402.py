# Generated by Django 2.2.11 on 2020-04-07 18:02
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0006_auto_20200407_1358"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumer", name="name", field=models.TextField(),
        ),
    ]