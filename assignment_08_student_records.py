# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
# =============================================================================

def display_menu():
    """Prints the main menu."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    """Returns the average of a list of scores, rounded to 2 decimal places."""
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def add_student(students):
    """Prompts for a student's name, ID, and scores, then saves the record."""
    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)

    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Prints a formatted table of all students, including their average score."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average'}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(str(int(s) if s == int(s) else s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average}")

    print("-" * 50)


def find_student_by_id(students, student_id):
    """Returns the student dict matching the given ID, or None if not found."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def show_average_for_student(students):
    """Asks for a student ID and displays that student's average score."""
    student_id = int(input("Enter student ID: "))
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Error: No student found with that ID.")
        return

    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average}")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            show_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")

        print()  # blank line for readability between menu cycles


if __name__ == "__main__":
    main()
