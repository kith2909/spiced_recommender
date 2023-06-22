from django.db import models
from django.utils import timezone
from django.db import models
import datetime
from django.contrib import admin


class Profile(models.Model):
    user_id = models.TextField()
    skills = models.TextField(default='')  # Based on test results
    goal = models.TextField(default='')  # Based on prediction
    goal_extra = models.TextField(default='')  # Based on prediction
    age = models.IntegerField(default=0)
    hobbies = models.TextField(default='')  # Based on test results
    location = models.TextField(default='')  # Based on test results
    language = models.TextField(default='')  # Based on test results
    img = models.TextField(default='')  # Based on prediction
    advice = models.BooleanField(default=False)  # Based on chat_ai
    advice_text = models.TextField(default='')  # Based on chat_ai


class ChatMessage(models.Model):
    user_id = models.TextField()
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hobbies = models.TextField(default='')
    mean_age = models.IntegerField(default=100)
    work_in_team = models.BooleanField(default=False)
    stubbornness_rate = models.IntegerField(default=0)
    location = models.TextField(default='Berlin, Germany')
    subjects = models.TextField(default='')
    feedback = models.TextField(default='')
    lang = models.TextField(default='')
    responsible = models.TextField(default='')
    logic_1 = models.IntegerField(default=0)
    logic_2 = models.IntegerField(default=0)
    tech_1 = models.IntegerField(default=0)
    tech_2 = models.IntegerField(default=0)


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

'''
class Question(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    hobbies = models.TextField(default='')
    mean_age = models.IntegerField(default=0)
    work_in_team = models.BooleanField(default=False)
    stubbornness_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    def get_type(self):
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
    user_id = models.TextField()

    # Fields specific to different types of answers
    is_checked = models.BooleanField(default=False)  # For type 1 (Checkbox choose y/n)
    numeric_answer = models.IntegerField(null=True, default=0)  # For type 2 (Answer should be a Number)
    text_answer = models.CharField(max_length=200, default=False)  # For type 3 (Answer should be a Text)
    grade = models.IntegerField(null=True, default=0)  # For type 2 (Answer should be a Number)

    def __str__(self):
        return self.choice_text
'''