from django.contrib import admin
from .models import Hall
# Register your models here.


class HallAdmin(admin.ModelAdmin):
	list_display = ('id', 'raw', 'seat', 'status', 'user')
	list_display_links = ('id', 'seat', 'user')
	search_fields = ('user',)


admin.site.register(Hall, HallAdmin)
