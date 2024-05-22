from django.contrib import admin

from todo.models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "create_date", "task_status"]
    list_filter = ["task_status"]
    search_fields = ["content"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
