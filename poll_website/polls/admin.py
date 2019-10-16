from django.contrib import admin

from .models import Question, Choice

# Change site header 
admin.site.site_header = "Polling Website Admin"
admin.site.site_title = "Polling Website Admin Area"
admin.site.index_title = "Welcome to the Polling Admin Area"

# We want to have the coices within the questions admin screen
# We will use *Tabular inline* to do that
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),                        # Hanging comma
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# These are used to create new options but we do not want that 
#admin.site.register(Question)
#admin.site.register(Choice)