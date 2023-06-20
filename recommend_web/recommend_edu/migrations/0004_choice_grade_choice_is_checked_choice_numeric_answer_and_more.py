# Generated by Django 4.2.2 on 2023-06-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recommend_edu", "0003_chatmessage_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="grade",
            field=models.CharField(
                choices=[(-2, "-2"), (-1, "-1"), (0, "0"), (1, "1"), (2, "2")],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="choice",
            name="is_checked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="choice",
            name="numeric_answer",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="choice",
            name="text_answer",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="choice",
            name="user_id",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="long_test",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="question",
            name="type_answer",
            field=models.CharField(
                choices=[
                    ("1", "Checkbox choose y/n"),
                    ("2", "Answer should be a Number"),
                    ("3", "Answer should be a Text"),
                    ("5", "Chose your grade"),
                ],
                default="1",
                max_length=1,
            ),
        ),
    ]