# Generated by Django 4.1.7 on 2023-03-01 08:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("issue_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="issue",
            old_name="type",
            new_name="type_old",
        ),
    ]
