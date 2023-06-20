from django.db import models
from django.utils import timezone
from django.db import models
import datetime
from django.contrib import admin


class ChatMessage(models.Model):
    user_id = models.TextField()
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


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

    def __str__(self):
        return self.question_text

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

    def __str__(self):
        return self.choice_text