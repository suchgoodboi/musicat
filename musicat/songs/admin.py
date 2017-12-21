from django.contrib import admin

from songs import models


class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'group',
        'description',
    )


admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Group)