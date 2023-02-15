from django.contrib import admin
from .models import Hall, Session, Tickets


class HallAdmin(admin.ModelAdmin):
	list_display = ('id', 'raw', 'seat', 'status', 'user', 'session')
	list_display_links = ('id', 'seat', 'user', 'session')
	search_fields = ('user',)


class SessionAdmin(admin.ModelAdmin):
	list_display = ('id', 'time', 'movie')
	list_display_links = ('id', 'time')
	search_fields = ('time', 'movie')


class TicketsAdmin(admin.ModelAdmin):
	list_display = ('id', 'seat_id', 'raw', 'seat', 'user', 'time')
	list_display_links = ('id', 'seat', 'user', 'time')
	search_fields = ('user',)


admin.site.register(Hall, HallAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Tickets, TicketsAdmin)