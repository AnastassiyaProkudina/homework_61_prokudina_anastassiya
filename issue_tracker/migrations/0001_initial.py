# Generated by Django 4.1.7 on 2023-03-01 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Status",
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
                ("name", models.CharField(max_length=50, verbose_name="Статус")),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Название"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Type",
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
                ("name", models.CharField(max_length=50, verbose_name="Тип")),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Название"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
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
                (
                    "summary",
                    models.CharField(
                        default="No summary", max_length=200, verbose_name="Заголовок"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=3000, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время обновления"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Удалено"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        default=None, null=True, verbose_name="Дата и время удаления"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Статус",
                        to="issue_tracker.status",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Тип",
                        to="issue_tracker.type",
                    ),
                ),
            ],
        ),
    ]