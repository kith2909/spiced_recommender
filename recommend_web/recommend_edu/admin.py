from django.contrib import admin

from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Job
from .models import ChatMessage

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Job)
admin.site.register(ChatMessage)