from django.contrib import admin

# Register your models here.

from django.contrib import admin

admin.site.site_header = "My Quiz App Admin"
admin.site.site_title = "Quiz App Admin Portal"
admin.site.index_title = "Welcome to Quiz App Dashboard"

# quiz/admin.py
from django.contrib import admin
from .models import *

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)

@admin.register(Clanguage_Question)
class Clanguage_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
    
@admin.register(Cpp_Question)
class Cpp_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
    
@admin.register(Java_Question)
class Java_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
    
@admin.register(Python_Question)
class Python_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)

@admin.register(PHP_Question)
class PHP_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
    
@admin.register(HTML_Question)
class HTML_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
    
@admin.register(Javascript_Question)
class Javascript_QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_answer')
    search_fields = ('question_text',)
    