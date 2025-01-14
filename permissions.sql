/*
Created by: Jerryline Pierre
Created date: Week 1 Module
Description: Inside your permissions.sql file, create three roles for your database.  
The first will be called admin_role and you will grant it access to the entire database
 with the option to grant privileges to other users.  The next role will be read_role and 
 it will be granted the privilege to read but not modify any database in the system.  
 The last role will be the modify_role and it will be granted privileges to modify any database on the system.
Grant the corresponding role to each user.  admin_role -> admin_user, read_role -> read_user, 
and modify_role -> modify user.  Don't forget to set the default role for each user!! 
*/
USE School;


DROP ROLE IF EXISTS 'admin_role';
CREATE ROLE 'admin_role';
GRANT ALL PRIVILEGES ON school.* TO 'admin_role';
GRANT 'admin_role' TO 'admin_user';
SET DEFAULT ROLE 'admin_role' TO 'admin_user';
FLUSH PRIVILEGES;


DROP ROLE IF EXISTS 'read_role';
CREATE ROLE 'read_role';
GRANT SELECT ON school.* TO 'read_role';
GRANT 'read_role' TO 'read_only';
GRANT execute on function school.getTeacherId TO 'read_only';
GRANT EXECUTE ON procedure school.getAllStudents TO 'read_only';
GRANT EXECUTE ON procedure school.getTeacherStudents To 'read_only';
GRANT EXECUTE ON PROCEDURE school.TeacherStudents TO 'read_only';
SET DEFAULT ROLE 'read_role' TO 'read_only';
FLUSH PRIVILEGES;


DROP ROLE IF EXISTS 'modify_role';
CREATE ROLE 'modify_role';
GRANT UPDATE, INSERT, ALTER, DELETE ON school.* TO 'modify_role' ;
GRANT 'modify_role' TO 'modify_user';
GRANT execute on function school.addStudent TO 'modify_role';
GRANT execute on function school.getTeacherId TO 'modify_role';
GRANT EXECUTE ON procedure school.getAllStudents TO 'modify_role';
GRANT EXECUTE ON procedure school.getTeacherStudents To 'modify_role';
GRANT EXECUTE ON PROCEDURE school.TeacherStudents TO 'modify_role';
SET DEFAULT ROLE 'modify_role' TO 'modify_user';
FLUSH PRIVILEGES;
