from django.contrib import admin

from users.models import OwnerProfile


class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'date_joined',
                    'last_login')


admin.site.register(OwnerProfile, OwnerProfileAdmin)
