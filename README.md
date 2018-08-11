requrements:

python >= 3.6.6

postgres >= 10.4

install steps:

psql -U postgres -f init.sql

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser --email admin@example.com --username admin


TODO

- tests all routers
- user attributes
- invites
- filters(serializers)
- ordrering
- documentation(api)
