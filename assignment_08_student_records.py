def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def add_student(students):
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    try:
        count = int(input("How many scores? "))
    except ValueError:
        print("Invalid score count.")
        return

    if count <= 0:
        print("Score count must be positive.")
        return

    scores = []
    for i in range(1, count + 1):
        while True:
            try:
                score = int(input(f"Enter score {i}: "))
                break
            except ValueError:
                print("Please enter a valid score.")
        scores.append(score)

    student = {"name": name, "id": student_id, "scores": scores}
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 60)
    print(f"{'Name':<15} {'ID':<10} {'Scores':<20} {'Average'}")
    print("-" * 60)
    for student in students:
        scores_text = ", ".join(str(score) for score in student["scores"])
        average_score = calculate_average(student["scores"])
        print(f"{student['name']:<15} {student['id']:<10} {scores_text:<20} {average_score:.2f}")
    print("-" * 60)


def calculate_student_average(students):
    student_id = input("Enter student ID: ").strip()
    for student in students:
        if student["id"] == student_id:
            average_score = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average_score:.2f}")
            return
    print("Student ID not found.")


def main():
    students = []

    while True:
        print("===============================")
        print("STUDENT RECORD SYSTEM MENU")
        print("===============================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

