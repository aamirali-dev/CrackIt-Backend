from django.contrib import admin
from .models import QuestionCategory, Question, Solution

admin.site.register(QuestionCategory)
admin.site.register(Solution)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_filter = ['category'] 


