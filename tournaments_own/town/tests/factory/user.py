import factory
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.sequence(lambda i: 'name_{}'.format(i)) 
    password = 'password'
    is_active = True
    is_staff = True
    is_superuser = True

    class Meta:
        model = User
