from django.contrib import admin
from .models import Job, JobNote, Builder


# Register your models here.

class JobNoteInLine(admin.StackedInline):
    model = JobNote
    extra = 1


class JobAdmin(admin.ModelAdmin):
    inlines = [JobNoteInLine]
    list_display = ('job_name', 'builder', 'job_address', 'job_city')
    list_filter = ['builder', 'job_city']
    search_fields = ['job_name', 'job_address', 'customer_name']


admin.site.register(Job, JobAdmin)
# admin.site.register(JobNote)
admin.site.register(Builder)
