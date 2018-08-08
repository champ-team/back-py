from django.contrib import admin
from tournaments_own.town.models import (
    UserAttribute, Game, Team, Tournament, TeamStat, PlayerStat
)

admin.site.register(UserAttribute)
admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(TeamStat)
admin.site.register(PlayerStat)
