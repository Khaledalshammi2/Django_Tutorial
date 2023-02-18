from django.contrib import admin
from .models import Question,Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # fields = ['pub_date', 'question_text']
    search_fields = ['question_text']
    list_filter = ['pub_date']
    fieldsets = [
        (None, 
         {'fields': ['question_text']}
        ),
        ('Date Information', 
         {'fields': ['pub_date'], 'classes': ['collapse']}
        ),
    ]
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)