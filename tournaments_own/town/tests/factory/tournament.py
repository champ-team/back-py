import factory
import datetime
import pytz
from tournaments_own.town.models import Tournament

class TournamentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Tournament
