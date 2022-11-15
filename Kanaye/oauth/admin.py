from django.contrib import admin

from oauth.models import AuthUser


@admin.register(AuthUser)
class UserAdmin(admin.ModelAdmin):
    pass
