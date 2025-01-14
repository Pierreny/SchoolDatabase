use School;
select * 
FROM
 Student;

SELECT 
 t.teacher_id,t.teacher_first_name,t.teacher_last_name,c.subject,c.room_number
FROM 
 teacher as t
INNER JOIN 
 classes  as c on t.teacher_id = c.teacher_id;


SELECT 
 first_name , last_name , student_grade
FROM 
 Student
ORDER BY 
  first_name asc;


SELECT 
    student.first_name AS StudentFirstName,
    Student.last_name AS StudentLastName,
    Teacher.teacher_first_name AS TeacherFirstName,
    Teacher.teacher_last_name AS TeacherLastName,
    Classes.subject,
    Classes.room_number
FROM 
    Student
INNER JOIN 
    ClassEnrollment ON Student.id = ClassEnrollment.id
INNER JOIN 
    Classes ON ClassEnrollment.class_id = Classes.class_id
INNER JOIN 
    Teacher ON Classes.teacher_id = Teacher.teacher_id;
/*week 3*/
 
Select 
s.first_name,s.last_name,c.subject,student_grade,t.teacher_first_name,t.teacher_last_name,t.teacher_email,s.student_grade

from student as s
inner join classenrollment AS cl ON  cl.ID = s.ID
inner join classes as c on cl.Class_id = c.Class_id
inner join teacher as t on c.teacher_id = t.teacher_id
order by s.student_grade ASC,
s.first_name;


select addStudent('Thomas','Henry','henry@gmail.com','2003-01-05','A');
select * from teacher;
select getTeacherId('Adam','Kessler');
call getAllStudents();
call getTeacherStudents('andrew', 'Jackson');
