from django.contrib import admin

from models import Stream

class StreamAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created_at', 'photo', 'tweet')

admin.site.register(Stream, StreamAdmin)
