# Generated by Django 4.2.2 on 2023-06-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "recommend_edu",
            "0004_choice_grade_choice_is_checked_choice_numeric_answer_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="grade",
            field=models.CharField(
                choices=[(-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2)],
                max_length=2,
                null=True,
            ),
        ),
    ]