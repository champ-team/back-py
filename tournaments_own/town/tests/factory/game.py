import factory
import datetime
import pytz
from tournaments_own.town.models import Game

class GameFactory(factory.django.DjangoModelFactory):
    map_name = factory.Faker('word')
    server_name = factory.Faker('word')
    server_password = factory.Faker('word')
    start_time = factory.Faker('date_time', tzinfo=pytz.UTC)

    class Meta:
        model = Game
