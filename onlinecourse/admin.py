from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'image', 'description']
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']


class LessonAdmin(admin.ModelAdmin):
    fields = ['title', 'course', 'order', 'content']
    list_display = ['title']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)