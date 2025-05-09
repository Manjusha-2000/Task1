def main():
    students = {}

    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add a student")
        print("2. Add grades for a student")
        print("3. View student average")
        print("4. View all students and grades")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            if name in students:
                print("Student already exists.")
            else:
                students[name] = {}
                print(f"Student '{name}' added.")

        elif choice == '2':
            name = input("Enter student name: ")
            if name not in students:
                print("Student not found.")
            else:
                subject = input("Enter subject: ")
                try:
                    grade = float(input("Enter grade: "))
                    students[name][subject] = grade
                    print(f"Added grade {grade} for {subject}.")
                except ValueError:
                    print("Invalid input. Grade must be a number.")

        elif choice == '3':
            name = input("Enter student name: ")
            if name not in students:
                print("Student not found.")
            else:
                grades = students[name].values()
                if grades:
                    average = sum(grades) / len(grades)
                    print(f"{name}'s average grade is: {average:.2f}")
                else:
                    print("No grades found for this student.")

        elif choice == '4':
            if not students:
                print("No student records available.")
            else:
                for name, subjects in students.items():
                    print(f"\n{name}'s Grades:")
                    for subject, grade in subjects.items():
                        print(f"  {subject}: {grade}")
                    if subjects:
                        avg = sum(subjects.values()) / len(subjects)
                        print(f"  Average: {avg:.2f}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
