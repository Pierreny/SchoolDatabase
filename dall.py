from binascii import Error
import mysql.connector



def get_db_connection():
    """Function to establish a connection to the MySQL database."""
    try:
        # Create a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password= 'root@12345',
            database='School'
        )
        
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Connection failed")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None

class Student:
     def __init__(self,first_name, last_name,email_address,date_of_birth, student_grade):
         self.first_name = first_name
         self.last_name = last_name
         self.email_address = email_address
         self.date_of_birth = date_of_birth
         self. student_grade = student_grade
     @staticmethod
     def read_only():
         connection = get_db_connection()
         students =[]
         if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM STUDENT"
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                for student in result:
                    students.append(f"ID: {student[0]},  NAME: {student[1]}  {student[2]}, EMAIL: {student[3]}, DATE OF BIRTH: {student[4]}, GRADE: {student[5]}")
  
            except mysql.connector.Error as error:
              print(f"Error: {error}")
            cursor.close()
            connection.close()
            return students
         else:
            print("Failed to connect to database")
            return []


     def add_student(self):
        connection = get_db_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """INSERT INTO Student (first_name, last_name, email_address, date_of_Birth, student_grade)
                        VALUES (%s, %s, %s, %s, %s)"""
            values = (self.first_name, self.last_name, self.email_address, self.date_of_birth, self.student_grade)

                # Execute query and commit transaction
            cursor.execute(query, values)
            connection.commit()
            print(f"Student  {self.first_name} {self.last_name} was added")

            cursor.close()
            connection.close()
        else:
            print("Failed to  connect to the database")
     
class Teacher:
    def __init__ (self,teacher_id,teacher_first_name,teacher_last_name,teacher_email):
        self.teacher_id = teacher_id
        self.teacher_first_name = teacher_first_name
        self.teacher_last_name = teacher_last_name
        self.teacher_email = teacher_email
    def add_teacher(self):
        connection = get_db_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """INSERT INTO Teacher(teacher_id,teacher_first_name,teacher_last_name,teacher_email) values(%s,%s,%s,%s)"""
            values = (self.teacher_id,self.teacher_first_name,self.teacher_last_name,self.teacher_email)
            cursor.execute(query,values)
            connection.commit()
            print(f"{self.teacher_last_name} Teacher was added" )
        else:
            print("Cannot add Teacher")

    def get_all_teacher(self):
        connection = get_db_connection()
        teachers = []
        if connection is not None:
            cursor = connection.cursor()
            query ="SELECT * FROM teacher"
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                for teacher in result:
                    teachers.append(f"ID: {teacher[0]}, Name: {teacher[1]} {teacher[2]}, Email: {teacher[3]}")


            except mysql.connector.Error as err:
                print(f"Error : {err}")
            cursor.close()
            connection.close()
            return teachers
        else:
            print("Cannot connect to the database")
            return []

        

class Classes:
    def __init__ (self, class_id, subject,teacher_id, room_number):
        self.class_id = class_id
        self.subject  = subject
        self.teacher_id = teacher_id
        self.room_number = room_number

    def add_classes(self):
        """Adds a new class record to the Classes table."""
        connection = get_db_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """INSERT INTO Classes(class_id,subject,teacher_id,room_number)
            VALUES (%s, %s, %s, %s)"""
            values = (self.class_id, self.subject, self.teacher_id, self.room_number)
            cursor.execute(query, values)
            connection.commit() 
            print(f"Class {self.class_id} added successfully.")
            cursor.close()
            connection.close()
        else:
                print("Could not add to Classes due to database connection issue.")

    def get_classes(self):
        """Fetches all class records from the Classes table."""
        connection = get_db_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM Classes"
                cursor.execute(query)
                result = cursor.fetchall() 
                return result
            except Error as e:
                print(f"Error fetching classes: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            print("Could not fetch classes due to database connection issue.")
            return []
        
class Classenrollment:
    def __init__ (self , Class_id, ID):
        self.class_id = Class_id
        self.ID = ID

    def get_class_enrollments(self):
       classenrollments = []
       connection = get_db_connection()
       if connection is not None:
        cursor = connection.cursor()
        # Query to fetch all class enrollments
        query = "SELECT * FROM classenrollment"
        try:
                cursor.execute(query)
                result = cursor.fetchall()  # Fetch all results
                for classenrollment in result:
                    print(classenrollment)
                connection.close()
                return result
        except mysql.connector.Error as err:
                print(f"Error fetching class enrollments: {err}")
                cursor.close()  # Close cursor
                connection.close()  # Close connection
                return classenrollments  # Return the formatted results
       else:
            print("Failed to connect to the database")
            return []  

    def add_enrollment(self):
        connection = get_db_connection()
        if connection is not None:
            cursor = connection.cursor()

            query = """INSERT  INTO classenrollment (class_id, ID)
                    VALUES (%s, %s)"""
            values = (self.class_id, self.ID)
            try:
                cursor.execute(query, values)
                connection.commit()  
                print(f"Student {self.ID} enrolled in class {self.class_id}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            connection.close()
        else:
            print("Cannot add to Database")
    

def main():
    while True:
      print("Main Menu:")
      print("1: View all Students")
      print("2: Add a Student")
      print("3: View all Teachers")
      print("4: Add a Teacher")
      print("5: View all Classes")
      print("6: Add a Class")
      print("7: View Class Enrollments")
      print("8: Enroll student to a class ")
      print("9: Exit")

      choice = input("Enter your choice (1-9): ")
      if choice == '1':
            studentone = Student('', '', '', '', '')
            students = studentone.read_only()
            print("Students in the database:")
            for student in students:
                print(student)
      elif choice =='2':
         while True:
            try:
            
                first_name = input("Enter student's first name: ")
                last_name = input("Enter student's last name: ")
                email_address = input("Enter student's email: ")
                date_of_birth = input("Enter student's date of birth (YYYY-MM-DD): ")
                student_grade = input("Enter student's grade: ")
                studentone = Student(first_name, last_name, email_address, date_of_birth, student_grade)
                studentone.add_student()
                break
            except ValueError:
                print("Invalid input")

      elif choice== '3':
        teacher1 = Teacher(0, "","","")
        teachers = teacher1.get_all_teacher()
        for teacher in teachers:
            print(teacher)

      elif choice == '4':
       while True:
            try:
                teacher_id = int(input("Enter the Teacher ID: "))
                teacher_first_name = input("Enter teachers first name: ")
                teacher_last_name = input("Enter teachers last name: ")
                teacher_email = input("Enter teachers email address: ")
                teacher = Teacher(teacher_id ,teacher_first_name,teacher_last_name,teacher_email)
                teacher.add_teacher()
                break
            except ValueError:
                print("Invalid input")

      elif choice == '5':
        class1= Classes(0,"",0,0)
        class2 = class1.get_classes()
        for char in class2:
            print(char)
            
      elif choice =='6':  
        while True:
            try:
                #class_id =int(input("Enter the class ID: "))
                #subject = input("Enter a subject: ")
                #teacher_id = int(input("Enter teacher ID: "))
                #room_number = int(input("Enter room number: "))
                class3 = Classes(class_id=6008, subject="Math", teacher_id=14, room_number=202)
                class3.add_classes()
                break

            except ValueError:
             print("Invalid input")

      elif choice =='7':
        classenroll = Classenrollment(0,0)
        classenrolls= classenroll.get_class_enrollments()

      elif choice == '8':
        while True:
            try:
                class_id = int(input("Enter class id: "))
                ID = int(input("Enter student ID: "))
                enroll= Classenrollment(class_id,ID)
                enroll.add_enrollment()
                break

            except ValueError:
             print("Invalid input")
      elif choice =='9':
        quit()
        break

      else:
        print("Invalid Choice")



if __name__ == "__main__":
    main()
