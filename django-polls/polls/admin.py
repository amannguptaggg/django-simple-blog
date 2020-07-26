from django.contrib import admin
from .models import Questions,Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Set', {
            'fields':['question_text']
        }),
        ('Date information',{
            'fields':['pub_date'],
        'classes': ['collapse']
        })
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'was_published_recently', 'pub_date')

admin.site.register(Questions,QuestionsAdmin)
