/*
Created by: Jerryline Pierre
create date : Week 1 Database Principles
Description :  Inside your users.sql file, create three users for your database. 
The first will be named admin_user with a password of admin1234, the next will be read_only with a password of read1234, 
and the last will be modify_user with a password of modify1234. 
Set this up so that the user can be used on any ip address that requests access to the database with the correct password.
*/

DROP USER IF EXISTS 'admin_user'; CREATE USER  'admin_user' IDENTIFIED BY  'admin1234';

DROP USER IF EXISTS 'read_only'; CREATE USER  'read_only'  IDENTIFIED BY 'read1234';

DROP USER IF EXISTS 'modify_user' ; CREATE USER 'modify_user' IDENTIFIED BY 'modify1234';
