USE SCHOOL;
DROP FUNCTION IF EXISTS addStudent;
DELIMITER $$

CREATE FUNCTION addStudent(
    first_name VARCHAR(50), 
    last_name VARCHAR(50), 
    email_address VARCHAR(100), 
    date_of_Birth DATE, 
    student_grade VARCHAR(1)
)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    INSERT INTO Student(first_name, last_name, email_address, date_of_Birth, student_grade)
    VALUES (first_name, last_name, email_address, date_of_Birth, student_grade);
    
    RETURN first_name;
END$$
DELIMITER ;


-- Drop the getTeacherId function if it exists
DROP FUNCTION IF EXISTS getTeacherId;
DELIMITER $$

CREATE FUNCTION getTeacherId(
    first_name VARCHAR(50), 
    last_name VARCHAR(50)
)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE id INT;
    
    SELECT teacher_id INTO id
    FROM Teacher
    WHERE LOWER(teacher_first_name) = LOWER(first_name) 
      AND LOWER(teacher_last_name) = LOWER(last_name);
      
    RETURN id;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS 
 getAllStudents;
DELIMITER $$
CREATE PROCEDURE 
 getAllStudents()
BEGIN
    SELECT * 
    FROM student;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS getTeacherStudents;
DELIMITER $$

CREATE PROCEDURE getTeacherStudents(
    first_name VARCHAR(50), 
    last_name VARCHAR(50)
)
BEGIN
    DECLARE teacher_id INT;
    SELECT getTeacherId(first_name, last_name) INTO teacher_id;

    SELECT s.first_name, s.last_name
    FROM Teacher AS t
    INNER JOIN Classes AS c ON t.teacher_id = c.teacher_id
    INNER JOIN ClassEnrollment AS cl ON c.Class_id = cl.Class_id
    INNER JOIN Student AS s ON cl.ID = s.ID
    WHERE t.teacher_id = teacher_id;

END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS TeacherStudents;

DELIMITER $$

CREATE PROCEDURE TeacherStudents()
BEGIN
    SELECT 
        s.first_name AS student_first_name, 
        s.last_name AS student_last_name, 
        t.teacher_first_name AS teacher_first_name, 
        t.teacher_last_name as teacher_last_name,
        c.subject, 
        s.student_grade
    FROM 
        Student AS s
    INNER JOIN ClassEnrollment AS cl ON s.ID = cl.ID
    INNER JOIN Classes AS c ON cl.class_id = c.class_id
    INNER JOIN Teacher AS t ON c.teacher_id = t.teacher_id;
END $$

DELIMITER ;
