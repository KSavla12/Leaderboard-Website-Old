from django.contrib import admin
from .models import Player_stats, Match_history
# Register your models here.

class MatchHistoryAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['date']}),
        (None,               {'fields': ['player_a']}),
        (None,               {'fields': ['player_a_score']}),
        (None,               {'fields': ['player_b']}),
        (None,               {'fields': ['player_b_score']}),
    ]

admin.site.register(Player_stats)
admin.site.register(Match_history, MatchHistoryAdmin)