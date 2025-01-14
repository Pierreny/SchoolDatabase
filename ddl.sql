CREATE database IF NOT exists SCHOOL;
use SCHOOL;

/**
SuperKeys
{Student_id},
{email_address},
{Student_id,email_address},
{Student_id,FirstName,LastName,Date_of_Birth}
Candidate Keys
{Student_id},
{email_address},
Primary key 
{Student_id},Because its unique and can easily be used to locate uple without dependency 
*/
CREATE TABLE if not exists  Student(
	ID INT  auto_increment primary key ,
	first_name varchar(50) not null,
	last_name varchar(50),
	email_address varchar(100),
	date_of_Birth date,
	student_grade varchar(1));
    
    
    
/**
Primary key 
  {teacher_id}, beacuse ids are different and cannot be duplicated because of auto increment
SuperKeys
	{teacher_id},
	{teacher_email},
	{teacher_id,teacher_email}
Candidate Keys
	{teacher_id},
	{teacher_email},

Primary key 
	{teacher_id},Because its unique and can easily be used to locate tuple without dependency 
*/
    
Create TABLE if not exists Teacher(
    teacher_id  int auto_increment PRIMARY KEY,
	teacher_first_name varchar(50),
	teacher_last_name varchar(50),
    teacher_email varchar(100));

/**
Primary key 
  {Class_id}, is introduced to uniquely indentify each classs
Super keys:
	{Class_id},
	{Class_id,subject},
	{teacher_id,class_id}
    {teacher_id,class_id,room_number}
Candidate Keys
	{Class_id},
	{Class_id,room_number},

Primary key 
	{class_id},Because its unique and can easily be used to locate tuple without dependency 
*/

CREATE TABLE if not exists Classes(
    Class_id int primary key ,
	subject varchar(100),
    teacher_id int ,
    room_number int,
    FOREIGN KEY (teacher_id) references Teacher(teacher_id));
/*
PRIMARY KEY 
	{class_id, id}
super key
   {class_id, id}
Candidate Keys
   {class_id, id}
*/
DROP TABLE IF EXISTS classcnrollment;

CREATE TABLE IF NOT EXISTS classenrollment (
    Class_id INT,
    ID INT,
    PRIMARY KEY (Class_id, ID),
    FOREIGN KEY (Class_id) REFERENCES Classes(Class_id),
    FOREIGN KEY (ID) REFERENCES Student(ID)
);
