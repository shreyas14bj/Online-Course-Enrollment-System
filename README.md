# Online-Course-Enrollment-System

This project is a simple Python-based system that allows students to enroll in courses, register, and view available courses. It uses `tkinter` for the GUI and stores data in CSV files.

## Features:
- Student Registration
- Course Enrollment
- View Courses
- Add Courses (Instructor)
- Data saved in CSV format

## Requirements:
- Python 3.x
- tkinter (included with Python)

1.  STUDENT_FILE.csv
Purpose: This file will store information about all registered students in the system.

Columns:

username: The unique username chosen by the student during registration.

password: The hashed or plain password of the student (if you are implementing password protection).

enrolled_courses: A list of Course IDs that the student has enrolled in, separated by commas. This helps to track which courses a student has enrolled in.

2. COURSE_FILE.csv
Purpose: This file will store information about all available courses in the system, including course details and the enrolled students.

Columns:

course_id: The unique identifier for each course.

course_name: The name of the course.

instructor: The name of the instructor teaching the course.

students_enrolled: A list of usernames of students enrolled in this course, separated by commas. This helps to track which students are taking each course.
