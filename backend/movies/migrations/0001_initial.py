# Generated by Django 5.2 on 2025-04-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tmdb_id", models.IntegerField(unique=True)),
                ("title", models.CharField(max_length=255)),
                ("overview", models.TextField(blank=True)),
                ("release_date", models.DateField(blank=True, null=True)),
                ("runtime", models.IntegerField(blank=True, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
                ("vote_count", models.IntegerField(blank=True, null=True)),
                ("poster_url", models.URLField(blank=True, max_length=500, null=True)),
                (
                    "backdrop_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
            ],
        ),
    ]
