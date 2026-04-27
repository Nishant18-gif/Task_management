from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'assigned_to', 'assigned_by', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')