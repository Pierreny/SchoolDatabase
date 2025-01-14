use School;

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('James','Harold','jharold@gmail.com','1995-10-24','A');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Jimmy','Harold','jmmyh@gmail.com','1995-10-15','B');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Chihi','sheila','jharold@gmail.com','1998-10-24','A');

/*WEEK 3 */

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('lisa','Moxley','lmoxley@gmail.com','2000-10-24','A');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('John','Smith','jsmith@gmail.com','1997-07-15','F');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Sarah','Nancy','nancyc@gmail.com','2001-01-24','A');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Justin','Lopez','jlopez@gmail.com','1992-10-1','B');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Vanessa','Green ','vgreen@gmail.com','2002-02-10','D');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Wade','Knicks','kwade@gmail.com','1996-10-20','C');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Juan','James','jjames@gmail.com','1996-09-01','D');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Quan','Cury','qcury@gmail.com','1993-10-19','B');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Vanesa','Henry','vhenry@gmail.com','2001-10-30','F');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Vicki','Smith','vsmith@gmail.com','1999-02-15','B');

insert into Student(first_name,last_name,email_address,date_of_Birth,student_grade)
values('Pierre','Cater','cp01@gmail.com','1996-10-02','A');


select * from Student;
/*
Inserting into Teacher table 
*/
INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('Adam','Kessler','akessler@gmail.com');

INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('Howard','James','hjames@gmail.com');

INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('Kate','Angelo','kangelo@gmail.com');

/*WEEK3*/

INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('Mercy','Perez','mperez@gmail.com');

INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('Brain','Mahoney','bmahoney.com');

INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('Andrew','Jackson','ajackson@gmail.com');

INSERT INTO Teacher(teacher_first_name,teacher_last_name,teacher_email)
values ('alba','Jefferies','ajefferies');

select* from Teacher;

/*
Inserting into Classes  table 
*/

Insert into classes(class_id,subject,teacher_id,room_number) 
values('6000','Litraeture','1','1');
Insert into classes(class_id,subject,teacher_id,room_number) 
values('6001','Computer Science','2','10');
Insert into classes(class_id,subject,teacher_id,room_number) 
values('6003','American Histroy','3','5');
/*WEEK3*/
Insert into classes(class_id,subject,teacher_id,room_number) 
values('6004','Math','4','4');
Insert into classes(class_id,subject,teacher_id,room_number) 
values('6005','Scieince','5','3');
Insert into classes(class_id,subject,teacher_id,room_number) 
values('6006',' Histroy','6','2');
Insert into classes(class_id,subject,teacher_id,room_number) 
values('6007','English','7','6');

select * from classes;

/*
Insert into Classenrollment
*/
Insert into classenrollment(Class_id,ID) 
VALUES ('6000',1);
Insert into classenrollment(Class_id,ID) 
VALUES ('6001',2);
Insert into classenrollment(Class_id,ID)
VALUES ('6003',3);
/*WEEK 3*/
Insert into classenrollment(Class_id,ID) 
VALUES ('6007',4);
Insert into classenrollment(Class_id,ID) 
VALUES ('6004',5);
Insert into classenrollment(Class_id,ID)
VALUES ('6005',6);
Insert into classenrollment(Class_id,ID) 
VALUES ('6006',7);
Insert into classenrollment(Class_id,ID) 
VALUES ('6007',8);
Insert into classenrollment(Class_id,ID)
VALUES ('6006',9);
Insert into classenrollment(Class_id,ID) 
VALUES ('6004',10);
Insert into classenrollment(Class_id,ID) 
VALUES ('6005',11);
Insert into classenrollment(Class_id,ID)
VALUES ('6007',12);
Insert into classenrollment(Class_id,ID) 
VALUES ('6006',13);
Insert into classenrollment(Class_id,ID) 
VALUES ('6005',14);
Insert into classenrollment(Class_id,ID)
VALUES ('6004',15);



SELECT *FROM classenrollment order by Class_id asc;
