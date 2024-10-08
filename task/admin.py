from django.contrib import admin

from task.models import Task, Attachment, TaskList


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'completed_by')


class TaskListAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'house')


class AttachmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Attachment, AttachmentAdmin)
