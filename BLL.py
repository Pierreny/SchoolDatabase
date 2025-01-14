import sys
import mysql.connector
from mysql.connector import Error

import dall


def call_get_teacher_id(teacher_first_name, teacher_last_name):
    connection = dall.get_db_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
          
            cursor.execute("SELECT getTeacherId(%s, %s)", (teacher_first_name, teacher_last_name))
            result = cursor.fetchone()  
            if result:
                print(f"Teacher Id: {result[0]}") 
                return result[0]  
            else:
                print("Teacher not found.")
                return None
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            return None
        finally:
            cursor.close()
            connection.close()
    else:
        print("Could not connect to the database.")
        return None
def call_get_all_students():
    connection = dall.get_db_connection()
    students = []
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.callproc("getAllStudents")
            results = cursor.stored_results()
            for result in results:
                for student in result.fetchall():
                 students.append(f"ID: {student[0]}, NAME: {student[1]} {student[2]}, EMAIL: {student[3]}, DATE OF BIRTH: {student[4]}, GRADE: {student[5]}")

        except mysql.connector.Error as error:
         print(f"Error: {error}")
        cursor.close()
        connection.close()
        return students
    
    else:
            print("Failed to connect to database")
            return []
    
def same_studentinfo():
    connection = dall.get_db_connection()
    studinfo = []
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.callproc("getAllStudents")
            results = cursor.stored_results()
            for result in results:
                for student in result.fetchall():
                    studinfo.append(f"NAME: {student[1]} {student[2]}, EMAIL: {student[3]}")
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            cursor.close()
            connection.close()
        return studinfo
    
    else:
        print("Failed to connect to database")
        return []

def callgetTeacherstudents():
    connection = dall.get_db_connection()
    Teacherstudent = []
    
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.callproc("TeacherStudents")
            
            results = cursor.stored_results()
            
            for result in results:
                for student in result.fetchall():
                    Teacherstudent.append(f"Student's Name:  {student[0]} {student[1]} Teacher's Name : {student[2]} {student[3]}, Subject: {student[4]}, GRADE: {student[5]}")
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            cursor.close()  
            connection.close()  
    
    return Teacherstudent  

def main():
    Teacinfo = callgetTeacherstudents()
    for t in Teacinfo:
        print(t)  

    studinfo = same_studentinfo()
    for char in studinfo:
        print(char)

    while True:
        try:        
            teacher_first_name = input("Enter teacher's first name: ")
            teacher_last_name = input("Enter teacher's last name: ")
            
        
            call_get_teacher_id(teacher_first_name, teacher_last_name)
            break

        except:
            print("Invalid input")
    

    print("All student by procedure ")
    students =call_get_all_students()
    for student in students:
        print(student)


    if __name__ == "__main__":
        dall.main()


main()
