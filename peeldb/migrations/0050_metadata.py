# Generated by Django 3.2.4 on 2021-06-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0049_user_agency_admin"),
    ]

    operations = [
        migrations.CreateModel(
            name="MetaData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=2000)),
                ("meta_title", models.CharField(max_length=2000)),
                ("meta_description", models.CharField(max_length=2000)),
                ("h1_tag", models.CharField(max_length=2000)),
            ],
        ),
    ]
