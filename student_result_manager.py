student = {}

while True:
    print("\n ----STUDENT MANAGER APP ----")
    print(("1. Add Student"))
    print(("2. View Student"))
    print(("3. Check Ressult"))
    print(("4. Exit"))

    choice = input("Enter Your Choice ! : ")

    # Add Student
    if choice == "1":
        name = input("Enter Student's name : ")
        marks = int(input("Enter Student's marks : "))
        student[name] = marks
        print(f"{name} Successfully Added !!")

    
    # View Students
    elif choice == "2":
        if not student:
            print("No student Found !")
        else:
            for name,marks in student.items():
                print(name, " : ", marks)

    # Check result 
    elif choice == "3":
        name = input("Enter Student's name : ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"{name} is PASSED ---")
            else:
                print(f"{name} is FAILED ---")    

        else:
            print("Student Not found !!")

    # Exiting
    elif choice == 4:
        print("---- Exiting ----")
        break
    else:
        print("In-valid Input ")