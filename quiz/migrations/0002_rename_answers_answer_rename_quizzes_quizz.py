# Generated by Django 5.2.3 on 2025-06-23 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Answers",
            new_name="Answer",
        ),
        migrations.RenameModel(
            old_name="Quizzes",
            new_name="Quizz",
        ),
    ]
