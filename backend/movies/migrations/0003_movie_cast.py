# Generated by Django 5.2 on 2025-04-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="cast",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
