from django.contrib import admin
from . import models

# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'role']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

admin.site.register(models.userProfileModel, profileAdmin)