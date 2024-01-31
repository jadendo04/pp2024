class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks
        print(f"Marks for {self.name} in {course_id} added successfully!")

    def display_info(self):
        print(f"Student ID: {self.student_id}\nName: {self.name}\nDate of Birth: {self.dob}")

    def show_marks_for_course(self, course_id):
        if course_id in self.marks:
            print(f"\nStudent: {self.name}\nCourse: {course_id}\nMarks: {self.marks[course_id]}")
        else:
            print(f"{self.name} has no marks for the selected course.")


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


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
    return Course(course_id, name)


def main():
    students = []
    courses = []

    num_students = get_number_of_students()
    for _ in range(num_students):
        students.append(get_student_info())

    num_courses = get_number_of_courses()
    for _ in range(num_courses):
        courses.append(get_course_info())

    while True:
        print("\nStudent Mark Management System")
        print("1. Add Marks for a Student")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Given Course")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            marks = float(input("Enter marks for the student in this course: "))

            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.add_marks(course_id, marks)
            else:
                print("Student not found.")

        elif choice == '2':
            print("List of Courses:")
            for course in courses:
                print(f"{course.course_id}. {course.name}")

        elif choice == '3':
            print("List of Students:")
            for student in students:
                student.display_info()
                print()

        elif choice == '4':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")

            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.show_marks_for_course(course_id)
            else:
                print("Student not found.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
