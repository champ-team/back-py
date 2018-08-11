import factory
import datetime
import pytz
from tournaments_own.town.models import Team
from tournaments_own.town.tests.factory import UserFactory

class TeamFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Team

    @factory.post_generation
    def tournaments(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tournament in extracted:
                self.tournaments.add(tournament)
