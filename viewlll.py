import tkinter as tk
from tkinter import StringVar, messagebox, scrolledtext

import mysql.connector
import dall
import BLL

class schooldbApp:
    def __init__(self, root):
        self.root = root
        self.root.title("School Database System")
        self.root.geometry("700x600")
        self.root.config(bg="Light gray")

        # Create frame
        self.mainframe = tk.Frame(self.root, bg="light gray")
        self.mainframe.pack()

        self.logindetails()


    def logindetails(self):
        
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        # Login title window
        Logintitle = tk.Label(self.mainframe, text="Login", bg="White", font=("sherif", 25))
        Logintitle.pack(pady=25)

        # Username label and entry
        usernamelabel = tk.Label(self.mainframe, text="Username")
        usernamelabel.pack(pady=10)
        self.username = StringVar()
        usernameEntry = tk.Entry(self.mainframe, textvariable=self.username)
        usernameEntry.pack(pady=10)

        # Password label and entry
        passwordlabel = tk.Label(self.mainframe, text="Password")
        passwordlabel.pack(pady=10)
        self.password = StringVar()
        passwordentry = tk.Entry(self.mainframe, textvariable=self.password, show="*") 
        passwordentry.pack(pady=10)

        # Login button
        loginButton = tk.Button(self.mainframe, text="Login", command=self.loginvalidate, bg="Light Blue")
        loginButton.pack(pady=20)


    def loginvalidate(self):
        """ Validates login by checking username, password and role from the database """
        username = self.username.get()
        password = self.password.get()

        
        if username and password:
            try:
             
                db = mysql.connector.connect(
                    host="localhost",          
                    user=username,             
                    password=password,          
                    database="School"           
                )

                if db.is_connected():
                    cursor = db.cursor()
                   
                    cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                    user_role = cursor.fetchone()

                    if user_role:
                        role = user_role[0]  
                        if role == 'admin':
                            messagebox.showinfo("Login Successful", "Welcome Admin!")
                            self.mainframe.destroy()
                            self.mainframe = tk.Frame(self.root, bg="Light Blue")
                            self.mainframe.pack(fill=tk.BOTH, expand=True)
                            self.buttonsOnHomeScreen() 
                        elif role == 'read_only':
                            messagebox.showinfo("Login Successful", "Welcome Read-Only User!")
                            self.mainframe.destroy()
                            self.mainframe = tk.Frame(self.root, bg="Light Blue")
                            self.mainframe.pack(fill=tk.BOTH, expand=True)
                            self.readonltbuttonsOnHomeScreen() 
                        elif role == 'modify_user':
                            messagebox.showinfo("Login Successful", "Welcome Modify User!")
                            self.mainframe.destroy()
                            self.mainframe = tk.Frame(self.root, bg="Light Blue")
                            self.mainframe.pack(fill=tk.BOTH, expand=True)
                            self.modifybuttonsOnHomeScreen() 
                        else:
                            messagebox.showerror("Login Failed", "Unknown role, contact administrator.")
                    else:
                        messagebox.showerror("Login Failed", "Username not found.")

                    db.close()
                else:
                    messagebox.showerror("Connection Error", "Failed to connect to the database.")

            except mysql.connector.Error as e:
                messagebox.showerror("Connection Error", f"Error: {e}")
                print(f"Error: {e}")



    def buttonsOnHomeScreen(self):
        # Title for application
        title = tk.Label(self.mainframe, text="School Database System",width=25,height= 3, font=("Sherif", 17), bg="White")
        title.pack(pady=25)

        # View student button
        self.viewStudent = tk.Button(self.mainframe, text="View Students", command=self.viewallStudents, width=20, height=3, bg="Light blue")
        self.viewStudent.pack(pady=10)

        # Add student button
        self.addstudent = tk.Button(self.mainframe, text="Add Student", width=20, height=3, command=self.addstudent, bg="Light blue")
        self.addstudent.pack(pady=10)

        #Button for student Teacher view
        self.TeacherStudentbutton = tk.Button(self.mainframe, text=" View Teacher and Student ", width=20, height=3, command=self.viewTeacherStudents, bg="Light blue")
        self.TeacherStudentbutton.pack(pady=10)

        
        self.allclassesbutton = tk.Button(self.mainframe, text="View Classes", command=self.allclasses, width=20, height=3, bg="Light blue")
        self.allclassesbutton.pack(pady=10)

       # View teacher ID button
        self.teacherIDbutton = tk.Button(self.mainframe, text="Get Teacher ID", command=self.viewteacher_id, width=20, height=3, bg="Light blue")
        self.teacherIDbutton.pack(pady=10)

    def modifybuttonsOnHomeScreen(self):
        title = tk.Label(self.mainframe, text="School Database System",width=25,height= 3, font=("Sherif", 17), bg="White")
        title.pack(pady=25)

        # View student button
        self.viewStudent = tk.Button(self.mainframe, text="View Students", command=self.viewallStudents, width=20, height=3, bg="Light blue")
        self.viewStudent.pack(pady=10)

        # Add student button
        self.addstudent = tk.Button(self.mainframe, text="Add Student", width=20, height=3, command=self.addstudent, bg="Light blue")
        self.addstudent.pack(pady=10)

        #Button for student Teacher view
        self.TeacherStudentbutton = tk.Button(self.mainframe, text=" View Teacher and Student ", width=20, height=3, command=self.viewTeacherStudents, bg="Light blue")
        self.TeacherStudentbutton.pack(pady=10)

        
        self.allclassesbutton = tk.Button(self.mainframe, text="View Classes", command=self.allclasses, width=20, height=3, bg="Light blue")
        self.allclassesbutton.pack(pady=10)

          # View teacher ID button
        self.teacherIDbutton = tk.Button(self.mainframe, text="Get Teacher ID", command=self.viewteacher_id, width=20, height=3, bg="Light blue")
        self.teacherIDbutton.pack(pady=10)

    def readonltbuttonsOnHomeScreen(self):
        # Title for application
        title = tk.Label(self.mainframe, text="School Database System",width=25,height= 3, font=("Sherif", 17), bg="White")
        title.pack(pady=25)

        # View student button
        self.viewStudent = tk.Button(self.mainframe, text="View Students", command=self.viewallStudents, width=20, height=3, bg="Light blue")
        self.viewStudent.pack(pady=10)

        #Add student button
        self.addstudent = tk.Button(self.mainframe, text="Add Student", width=20, height=3, command=self.addstudent, bg="Light blue")
        self.addstudent.pack(pady=10)

        #Button for student Teacher view
        self.TeacherStudentbutton = tk.Button(self.mainframe, text=" View Teacher and Student ", width=20, height=3, command=self.viewTeacherStudents, bg="Light blue")
        self.TeacherStudentbutton.pack(pady=10)

        self.allclassesbutton = tk.Button(self.mainframe, text="View Classes", command=self.allclasses, width=20, height=3, bg="Light blue")
        self.allclassesbutton.pack(pady=10)

          # View teacher ID button
        self.teacherIDbutton = tk.Button(self.mainframe, text="Get Teacher ID", command=self.viewteacher_id, width=20, height=3, bg="Light blue")
        self.teacherIDbutton.pack(pady=10)


    def viewallStudents(self):
        window = tk.Toplevel(self.root)
        window.title("View All Students")
        resulttext = scrolledtext.ScrolledText(window)
        resulttext.pack(pady=20)
        students = BLL.same_studentinfo()
        
        for student in students:
            resulttext.insert(tk.END,student + "\n") 

    def addstudent(self):
        addwindow = tk.Toplevel(self.root)
        addwindow.title("Add a New Student")

        # First name entry
        tk.Label(addwindow, text="First Name: ").grid(row=0, column=0, padx=10, pady=10)
        self.fnentry = tk.Entry(addwindow)
        self.fnentry.grid(row=0, column=1)

        # Last name entry
        tk.Label(addwindow, text="Last Name:").grid(row=1, column=0, padx=10, pady=10)
        self.lnentry = tk.Entry(addwindow)
        self.lnentry.grid(row=1, column=1)

        # Email address entry
        tk.Label(addwindow, text="Email Address:").grid(row=2, column=0, padx=10, pady=10)
        self.emailadd = tk.Entry(addwindow)
        self.emailadd.grid(row=2, column=1)

        # Date of Birth entry
        tk.Label(addwindow, text="Date of Birth (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=10)
        self.dob_entry = tk.Entry(addwindow)
        self.dob_entry.grid(row=3, column=1)

        # Grade entry
        tk.Label(addwindow, text="Grade:").grid(row=4, column=0, padx=10, pady=10)
        self.grade_entry = tk.Entry(addwindow)
        self.grade_entry.grid(row=4, column=1)

        # Submit button to add student
        self.submitbutton = tk.Button(addwindow, text="Add Student", command=self.submit_student)
        self.submitbutton.grid(row=5, column=0, columnspan=2, pady=10)

    def submit_student(self):
        first_name = self.fnentry.get()
        last_name = self.lnentry.get()
        email_address = self.emailadd.get()
        date_of_birth = self.dob_entry.get()
        grade = self.grade_entry.get()

        student = dall.Student(first_name, last_name, email_address, date_of_birth, grade)
        student.add_student()

     
        self.fnentry.delete(0, tk.END)
        self.lnentry.delete(0, tk.END)
        self.emailadd.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Student added successfully!")

    def viewTeacherStudents(self):
        window = tk.Toplevel(self.root)
        window.title(" View Teacher and Students ")
        resulttext = scrolledtext.ScrolledText(window )
        resulttext.pack(pady=20)
        students = BLL.callgetTeacherstudents()
        
        for student in students:
            resulttext.insert(tk.END,student + "\n")

    
    def allclasses(self):
        window = tk.Toplevel(self.root)
        window.title("All Classes")
        resulttext  = scrolledtext.ScrolledText(window)
        resulttext.pack(pady=20)
        classesall= dall.Classes.get_classes(self)
        if classesall:
            for clas in classesall:
                resulttext.insert(tk.END, f"Class ID: {clas[0]}, Class Name: {clas[1]}, Teacher ID: {clas[2]}, Room Number: {clas[3]}\n")
        else:
            resulttext.insert(tk.END, "No classes found.")


    def viewteacher_id(self):
        """ Display teacher ID based on first and last name """
        
        window = tk.Toplevel(self.root)
        window.title("Get Teacher ID")

       
        tk.Label(window, text="Teacher First Name:").grid(row=0, column=0, padx=10, pady=10)
        teacher_first_name = tk.Entry(window)
        teacher_first_name.grid(row=0, column=1)

       
        tk.Label(window, text="Teacher Last Name:").grid(row=1, column=0, padx=10, pady=10)
        teacher_last_name = tk.Entry(window)
        teacher_last_name.grid(row=1, column=1)

       
        result_text = scrolledtext.ScrolledText(window, height=5, width=40)
        result_text.grid(row=3, column=0, columnspan=2, pady=10)

        
        def get_teacher_id():
            first_name = teacher_first_name.get()
            last_name = teacher_last_name.get()

            
            if not first_name or not last_name:
                messagebox.showwarning("Input Error", "Please provide both first and last names.")
                return

            
            teacher_id = BLL.call_get_teacher_id(first_name, last_name)

            
            if teacher_id is None:
                result_text.insert(tk.END, "Teacher not found.\n")
            else:
                result_text.insert(tk.END, f"Teacher ID: {teacher_id}\n")

        # Button to get teacher ID
        tk.Button(window, text="Get Teacher ID", command=get_teacher_id).grid(row=2, column=0, columnspan=2, pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = schooldbApp(root)
    root.mainloop()
