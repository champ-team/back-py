from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from tournaments_own.town import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('teams', views.TeamViewSet)
router.register('games', views.GameViewSet)
router.register('tournaments', views.TournamentViewSet)
router.register('team-stats', views.TeamStatViewSet)
router.register('player-stats', views.PlayerStatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', auth_views.obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)