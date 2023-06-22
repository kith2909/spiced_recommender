# Generated by Django 4.2.2 on 2023-06-22 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatMessage",
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
                ("user_id", models.TextField()),
                ("user_message", models.TextField()),
                ("bot_response", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("company", models.CharField(max_length=300)),
                ("title", models.CharField(max_length=300)),
                ("category", models.CharField(max_length=300)),
                ("location", models.CharField(max_length=300)),
                ("responsibilities", models.TextField()),
                ("minimum_qualifications", models.TextField()),
                ("preferred_qualifications", models.TextField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("user_id", models.TextField()),
                ("skills", models.TextField(default="")),
                ("goal", models.TextField(default="")),
                ("goal_extra", models.TextField(default="")),
                ("age", models.IntegerField(default=0)),
                ("hobbies", models.TextField(default="")),
                ("location", models.TextField(default="")),
                ("language", models.TextField(default="")),
                ("img", models.TextField(default="")),
                ("advice", models.BooleanField(default=False)),
                ("advice_text", models.TextField(default="")),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("hobbies", models.TextField(default="")),
                ("mean_age", models.IntegerField(default=100)),
                ("work_in_team", models.BooleanField(default=False)),
                ("stubbornness_rate", models.IntegerField(default=0)),
                ("location", models.TextField(default="Berlin, Germany")),
                ("subjects", models.TextField(default="")),
                ("feedback", models.TextField(default="")),
                ("lang", models.TextField(default="")),
                ("responsible", models.TextField(default="")),
                ("logic_1", models.IntegerField(default=0)),
                ("logic_2", models.IntegerField(default=0)),
                ("tech_1", models.IntegerField(default=0)),
                ("tech_2", models.IntegerField(default=0)),
                (
                    "profile_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recommend_edu.profile",
                    ),
                ),
            ],
        ),
    ]