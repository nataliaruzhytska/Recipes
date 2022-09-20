create user recipes_admin password 'simplepass';

create database recipes_db encoding 'utf-8';
grant all privileges on database recipes_db to recipes_admin;
alter database recipes_db owner to recipes_admin;

create database recipes_test_db encoding 'utf-8';
grant all privileges on database recipes_test_db to recipes_admin;
alter database recipes_test_db owner to recipes_admin;

