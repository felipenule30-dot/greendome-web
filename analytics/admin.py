from django.contrib import admin
from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display  = ('page', 'ip_anonimizada', 'timestamp')
    list_filter   = ('timestamp',)
    search_fields = ('page', 'ip_anonimizada')
    readonly_fields = ('page', 'timestamp', 'user_agent', 'referrer', 'ip_anonimizada')
    ordering      = ('-timestamp',)

    def has_add_permission(self, request):
        return False
