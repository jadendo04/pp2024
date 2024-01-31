import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = None

    def add_marks(self, course_id, marks, credits):
        rounded_marks = math.floor(marks * 10) / 10  # Round down to 1-digit decimal
        self.marks[course_id] = {'marks': rounded_marks, 'credits': credits}
        print(f"Marks for {self.name} in {course_id} added successfully!")

    def calculate_gpa(self):
        if not self.marks:
            return 0.0

        total_credits = sum(course_info['credits'] for course_info in self.marks.values())
        weighted_sum = sum(course_info['marks'] * course_info['credits'] for course_info in self.marks.values())
        self.gpa = weighted_sum / total_credits if total_credits != 0 else 0.0
        return self.gpa

    def display_info(self):
        print(f"Student ID: {self.student_id}\nName: {self.name}\nDate of Birth: {self.dob}\nGPA: {self.gpa}")

    def show_marks_for_course(self, course_id):
        if course_id in self.marks:
            print(f"\nStudent: {self.name}\nCourse: {course_id}\nMarks: {self.marks[course_id]['marks']}")
        else:
            print(f"{self.name} has no marks for the selected course.")


def get_number_of_students():
    return int(input("Enter the number of students in a class: "))


def get_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    return Student(student_id, name, dob)


def get_number_of_courses():
    return int(input("Enter the number of courses: "))


def get_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    return {'id': course_id, 'name': name, 'credits': credits}


def calculate_average_gpa(student):
    gpa = student.calculate_gpa()
    print(f"Average GPA for {student.name}: {gpa}")


def main(stdscr):
    students = []
    courses = []

    num_students = get_number_of_students()
    for _ in range(num_students):
        students.append(get_student_info())

    num_courses = get_number_of_courses()
    for _ in range(num_courses):
        courses.append(get_course_info())

    while True:
        stdscr.clear()
        stdscr.addstr("Student Mark Management System\n")
        stdscr.addstr("1. Add Marks for a Student\n")
        stdscr.addstr("2. List Students\n")
        stdscr.addstr("3. Show Student Marks for a Given Course\n")
        stdscr.addstr("4. Calculate Average GPA for a Student\n")
        stdscr.addstr("5. Sort Students by GPA (Descending)\n")
        stdscr.addstr("6. Exit\n")

        choice = stdscr.getch() - ord('0')

        if choice == 1:
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            marks = float(input("Enter marks for the student in this course: "))
            credits = next((course_info['credits'] for course_info in courses if course_info['id'] == course_id), None)

            student = next((s for s in students if s.student_id == student_id), None)
            if student and credits is not None:
                student.add_marks(course_id, marks, credits)
            else:
                print("Student not found or course credits not defined.")

        elif choice == 2:
            for student in students:
                student.display_info()
                print()

        elif choice == 3:
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")

            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.show_marks_for_course(course_id)
            else:
                print("Student not found.")

        elif choice == 4:
            student_id = input("Enter student ID: ")
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                calculate_average_gpa(student)
            else:
                print("Student not found.")

        elif choice == 5:
            students.sort(key=lambda s: s.gpa, reverse=True)

        elif choice == 6:
            print("Exiting the program. Goodbye!")
