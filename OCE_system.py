import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.students = []
        self.grades = {}

class Student:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.enrolled_courses = []

    def check_password(self, password):
        return self.__password == password

class Instructor:
    def __init__(self, name, department):
        self.name = name
        self.department = department


students_db = {}
courses = {}
instructors = {
    "I001": Instructor("Dr. Smith", "Computer Science"),
    "I002": Instructor("Prof. John", "Mathematics")
}

STUDENT_FILE = "students.csv"
COURSE_FILE = "courses.csv"
DATA_FILE = "enrollment_data.csv"


def save_all_data():
    # Save students to CSV
    with open("STUDENT_FILE.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Password', 'Enrolled Courses'])
        for student in students_db.values():
            writer.writerow([student.username, student._Student__password, ",".join(student.enrolled_courses)])

    # Save courses to CSV
    with open("COURSE_FILE.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Course ID', 'Course Name', 'Instructor Name', 'Students', 'Grades'])
        for course in courses.values():
            writer.writerow([course.course_id, course.name, course.instructor.name, ",".join(course.students), json.dumps(course.grades)])


def load_all_data():
    # Load students from CSV
    if os.path.exists("STUDENT_FILE.csv"):
        with open("STUDENT_FILE.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                username, password, enrolled_courses = row
                student = Student(username, password)
                student.enrolled_courses = enrolled_courses.split(',')
                students_db[username] = student

    # Load courses from CSV
    if os.path.exists("COURSE_FILE.csv"):
        with open("COURSE_FILE.csv",'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                course_id, name, instructor_name, students, grades = row
                instr = next((i for i in instructors.values() if i.name == instructor_name), None)
                if not instr:
                    instr = Instructor(instructor_name, "Unknown")
                    instructors[f"I{len(instructors)+1:03}"] = instr
                course = Course(course_id, name, instr)
                course.students = students.split(',')
                course.grades = json.loads(grades)
                courses[course_id] = course


def register_student():
    name = simpledialog.askstring("Register", "Enter your name:")
    password = simpledialog.askstring("Register", "Set a password:", show='*')
    if name and password:
        if name in students_db:
            messagebox.showinfo("Info", "Student already registered.")
        else:
            students_db[name] = Student(name, password)
            messagebox.showinfo("Success", "Registration successful!")

def enroll_in_course():
    username = simpledialog.askstring("Login", "Enter your name:")
    password = simpledialog.askstring("Login", "Enter password:", show='*')
    student = students_db.get(username)
    if student and student.check_password(password):
        cid = simpledialog.askstring("Enroll", "Enter Course ID:")
        if cid in courses:
            course = courses[cid]
            if username not in course.students:
                course.students.append(username)
                student.enrolled_courses.append(cid)
                messagebox.showinfo("Success", f"Enrolled in {course.name}")
            else:
                messagebox.showinfo("Info", "Already enrolled")
        else:
            messagebox.showinfo("Error", "Course not found")
    else:
        messagebox.showinfo("Error", "Invalid login")

def view_courses():
    course_list = "\n".join([f"{cid}: {course.name} ({course.instructor.name})" for cid, course in courses.items()])
    messagebox.showinfo("Courses", course_list or "No courses available")

def add_course():
    cid = simpledialog.askstring("Add Course", "Course ID:")
    name = simpledialog.askstring("Add Course", "Course Name:")
    instructor_name = simpledialog.askstring("Add Course", "Instructor Name:")
    if cid and name and instructor_name:
        instr = next((i for i in instructors.values() if i.name == instructor_name), None)
        if not instr:
            instr = Instructor(instructor_name, "Unknown")
            instructors[f"I{len(instructors)+1:03}"] = instr
        courses[cid] = Course(cid, name, instr)
        messagebox.showinfo("Success", "Course added")


def main_gui():
    load_all_data()
    root = tk.Tk()
    root.title("Online Course Enrollment System")
    root.geometry("400x300")

    tk.Label(root, text="Welcome to Course System", font=('Arial', 14)).pack(pady=10)

    tk.Button(root, text="Register Student", command=register_student, width=30).pack(pady=5)
    tk.Button(root, text="Enroll in Course", command=enroll_in_course, width=30).pack(pady=5)
    tk.Button(root, text="View Courses", command=view_courses, width=30).pack(pady=5)
    tk.Button(root, text="Add Course (Instructor)", command=add_course, width=30).pack(pady=5)
    tk.Button(root, text="Exit & Save", command=lambda: [save_all_data(), root.destroy()], width=30).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main_gui()
