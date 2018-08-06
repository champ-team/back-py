CREATE USER town_user WITH password 'town_password';
CREATE DATABASE town_database OWNER town_user;
GRANT ALL ON DATABASE town_database TO town_user;