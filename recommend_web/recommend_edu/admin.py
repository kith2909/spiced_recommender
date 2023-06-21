from django.contrib import admin

from django.contrib import admin

from .models import Answer
from .models import Profile
from .models import Job
from .models import ChatMessage


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [AnswerInline]


admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(Job)
admin.site.register(ChatMessage)
