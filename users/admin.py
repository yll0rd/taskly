from django.contrib import admin

from users.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]


admin.site.register(Profile, ProfileAdmin)
