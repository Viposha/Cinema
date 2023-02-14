from django.contrib import admin
from .models import Hall


class HallAdmin(admin.ModelAdmin):
	list_display = ('id', 'raw', 'seat', 'status', 'user')
	list_display_links = ('id', 'seat', 'user')
	search_fields = ('user',)


admin.site.register(Hall, HallAdmin)
