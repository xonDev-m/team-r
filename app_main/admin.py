from django.contrib import admin
from .models import Task, TaskFile

class TaskFileInline(admin.TabularInline):
    model = TaskFile
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TaskFileInline]

admin.site.register(Task, TaskAdmin)
