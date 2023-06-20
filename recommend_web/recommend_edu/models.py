from django.db import models
from django.utils import timezone
from django.db import models
import datetime
from django.contrib import admin


class Person(models.Model):
    user_id = models.TextField()


class ChatMessage(models.Model):
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    hobbies = models.TextField()
    mean_age = models.IntegerField()
    work_in_team = models.BooleanField()
    stubbornness_level = models.IntegerField()


class Job(models.Model):
    company = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    responsibilities = models.TextField()
    minimum_qualifications = models.TextField()
    preferred_qualifications = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        out_str = f'{self.company} {self.title} {self.category} {self.location} {self.responsibilities} ' \
                  f'{self.minimum_qualifications} {self.preferred_qualifications} {self.salary}'
        return out_str


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    hobbies = models.TextField()
    mean_age = models.IntegerField()
    work_in_team = models.BooleanField()
    stubbornness_level = models.IntegerField()

    def __str__(self):
        return self.person

    def get_type(self):
        return self.person

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    user_id = models.TextField()

    # Fields specific to different types of answers
    is_checked = models.BooleanField(default=False)  # For type 1 (Checkbox choose y/n)
    numeric_answer = models.IntegerField(null=True, default=0)  # For type 2 (Answer should be a Number)
    text_answer = models.CharField(max_length=200, default=False)  # For type 3 (Answer should be a Text)
    grade = models.IntegerField(null=True, default=0)  # For type 2 (Answer should be a Number)

    def __str__(self):
        return self.choice_text
