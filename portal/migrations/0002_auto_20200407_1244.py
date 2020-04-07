# Generated by Django 2.2.11 on 2020-04-07 16:44
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="order", name="pre_packaged_meal_budget",),
        migrations.RemoveField(model_name="provider", name="email",),
        migrations.AddField(
            model_name="provider",
            name="able_to_prepare_prepacked_meals",
            field=models.NullBooleanField(
                verbose_name="Are you able to prepare individually packaged meals?"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="capacity_to_package_bulk",
            field=models.NullBooleanField(
                verbose_name="Do you have the capacity to package food in bulk?"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="marketing_email",
            field=models.TextField(
                blank=True, null=True, verbose_name="Marketing point person email"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="marketing_name",
            field=models.TextField(
                blank=True, null=True, verbose_name="Marketing point person name"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="operations_email",
            field=models.TextField(
                blank=True, null=True, verbose_name="Operations point person email"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="operations_name",
            field=models.TextField(
                blank=True, null=True, verbose_name="Operations point person name"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="safely_operate_kitchen",
            field=models.NullBooleanField(
                verbose_name="Will you be able to safely operate your kitchen?"
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="servings_per_shift",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="How many servings you can prepare on one shift if packaged in bulk?",
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="description",
            field=models.TextField(
                verbose_name="Please provide a name for your meal and a list of main ingredients"
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="name",
            field=models.TextField(verbose_name="Your Restaurant Name"),
        ),
        migrations.AlterField(
            model_name="provider",
            name="opening_hours",
            field=models.ManyToManyField(
                blank=True,
                to="portal.OpeningHours",
                verbose_name="List all available days of the week and times you could prepare and provide meals",
            ),
        ),
    ]