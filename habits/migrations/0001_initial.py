# Generated by Django 5.1.4 on 2024-12-04 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                    "place",
                    models.CharField(
                        max_length=200,
                        verbose_name="Место, в котором необходимо выполнять привычку",
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        verbose_name="Время, когда необходимо выполнять привычку"
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        max_length=200,
                        verbose_name="Действие, которое представляет собой привычка",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(verbose_name="Признак приятной привычки"),
                ),
                (
                    "frequency_number",
                    models.PositiveIntegerField(
                        verbose_name="Периодичность выполнения привычки для напоминания"
                    ),
                ),
                (
                    "frequency_unit",
                    models.CharField(
                        choices=[
                            ("minutes", "минуты"),
                            ("hours", "часы"),
                            ("days", "дни"),
                        ],
                        default="days",
                        max_length=10,
                        verbose_name="Единица периодичности выполнения привычки",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(
                        verbose_name="Время, которое предположительно потратит пользователь на выполнение привычки"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
