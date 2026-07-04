students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Records Found.")
        else:
            print("\nStudent Records:")
            for roll, details in students.items():
                print(f"Roll No: {roll}")
                print(f"Name: {details['Name']}")
                print(f"Marks: {details['Marks']}")
                print("----------------------")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("Student Found!")
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")