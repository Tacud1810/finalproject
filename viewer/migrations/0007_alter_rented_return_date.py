# Generated by Django 4.2.2 on 2023-07-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("viewer", "0006_alter_rented_rent_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rented",
            name="return_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]