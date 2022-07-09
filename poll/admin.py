from django.contrib import admin

from .models import Question, Choice
  
admin.site.site_header = "MaHa Admin"
admin.site.site_title = "MaHa Admin Area"
admin.site.index_title = "Welcome to the MaHa Admin Area"
  
  
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4
  
  
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['published_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]
  
  
admin.site.register(Question, QuestionAdmin)
