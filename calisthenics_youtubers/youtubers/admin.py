from django.contrib import admin
from .models import Youtuber

# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Youtuber, YoutuberAdmin)
