from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline): 
    model = Choice
    extra = 4  # Number of extra empty choice forms

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
