import sys

def title():
    print("===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Find Top Student")
    print("5. Search Student")
    print("6. Exit")


def add_student(students):
    name = input("Enter student name: ")
    python_grade = float(input("Enter student grade in Python: "))
    math_grade = float(input("Enter student grade in Math: "))
    physics_grade = float(input("Enter student grade in Physics: "))
    
    student = {
    "name": name,
    "python": python_grade,
    "math": math_grade,
    "physics": physics_grade
    }
    students.append(student)
    print(f"Student {name} added.")
    
def view_students(students):
    if not students:
        print("No students found.")
        return
    
    print("===== STUDENT LIST =====")
    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Python: {student['python']}, "
            f"Math: {student['math']}, "
            f"Physics: {student['physics']}"
        )
        
def calculate_average(students):
    if not students:
        print("No students found.")
        return
    
    total_python = sum(student['python'] for student in students)
    total_math = sum(student['math'] for student in students)
    total_physics = sum(student['physics'] for student in students)
    
    average_python = total_python / len(students)
    average_math = total_math / len(students)
    average_physics = total_physics / len(students)
    
    print(f"Average Python Grade: {average_python:.2f}")
    print(f"Average Math Grade: {average_math:.2f}")
    print(f"Average Physics Grade: {average_physics:.2f}")
    
def find_top_student(students):
    print("\n--- Top Student ---")

    if len(students) == 0:
        print("No students found.")
        return
    
    top_student = students[0]
    for student in students:
        if (student['python'] + student['math'] + student['physics']) > (top_student['python'] + top_student['math'] + top_student['physics']):
            top_student = student
    print(f"Top Student: {top_student['name']}")
    print(f"Average Grade: {(top_student['python'] + top_student['math'] + top_student['physics']) / 3:.2f}")
    
def search_student(students):
    name = input("Enter student name to search: ")
    found_students = [student for student in students if student['name'].lower() == name.lower()]
    
    if not found_students:
        print(f"No student found with name {name}.")
        return
    
    print(f"Found {len(found_students)} student(s) with name {name}:")
    for student in found_students:
        print(
            f"Name: {student['name']}, "
            f"Python: {student['python']}, "
            f"Math: {student['math']}, "
            f"Physics: {student['physics']}"
        )

def main():
    students = []
    
    while True:
        title()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            calculate_average(students)
        elif choice == '4':
            find_top_student(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            print("Exiting Student Grade Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()