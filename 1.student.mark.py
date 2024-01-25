def input_number_of_students():
    return int(input("Enter the number of students in a class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    return {'id': student_id, 'name': name, 'dob': dob, 'marks': {}}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return {'id': course_id, 'name': name}

def select_course_and_input_marks(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    marks = float(input("Enter marks for the student in this course: "))

    for student in students:
        if student['id'] == student_id:
            student['marks'][course_id] = marks
            print(f"Marks for {student['name']} in {course_id} added successfully!")
            break
    else:
        print("Student not found.")

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"{course['id']}. {course['name']}")

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"{student['id']}. {student['name']}")

def show_student_marks_for_given_course(students):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    for student in students:
        if student['id'] == student_id and course_id in student['marks']:
            print(f"\nStudent: {student['name']}\nCourse: {course_id}\nMarks: {student['marks'][course_id]}")
            break
    else:
        print("Student not found or has no marks for the selected course.")

def main():
    students = []
    courses = []

    num_students = input_number_of_students()
    for _ in range(num_students):
        students.append(input_student_information())

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        courses.append(input_course_information())

    while True:
        print("\nStudent Mark Management System")
        print("1. Select Course and Input Marks for a Student")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Given Course")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            select_course_and_input_marks(students, courses)

        elif choice == '2':
            list_courses(courses)

        elif choice == '3':
            list_students(students)

        elif choice == '4':
            show_student_marks_for_given_course(students)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
