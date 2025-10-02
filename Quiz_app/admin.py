from django.contrib import admin

# Register your models here.

from django.contrib import admin

admin.site.site_header = "My Quiz App Admin"
admin.site.site_title = "Quiz App Admin Portal"
admin.site.index_title = "Welcome to Quiz App Dashboard"

# quiz/admin.py
from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
