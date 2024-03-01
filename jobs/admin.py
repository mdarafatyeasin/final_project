from django.contrib import admin
from . import models

# Register your models here.
class jobCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category',)}

class jobCircularAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'post_date', 'last_date', 'vacancy', 'salary']

class jobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant']

admin.site.register(models.jobCategoryModel,jobCategoryAdmin)
admin.site.register(models.jobCircularModel,jobCircularAdmin)
admin.site.register(models.jobApplicationModel,jobApplicationAdmin)