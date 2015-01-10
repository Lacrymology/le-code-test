from django.contrib import admin

from models import PhotoItem, TweetItem

class ItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'deleted',)
    list_editable = ('deleted',)

admin.site.register(PhotoItem, ItemAdmin)
admin.site.register(TweetItem, ItemAdmin)
