CREATE USER town_user WITH password 'town_password';
ALTER USER town_user CREATEDB;
CREATE DATABASE town_database OWNER town_user;
GRANT ALL ON DATABASE town_database TO town_user;