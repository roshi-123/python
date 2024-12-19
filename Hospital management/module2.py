import module1 as m1
def doctor_login():
    print("\nWelcome to Doctor Login Page.")
    email = input("Enter your login ID: ").strip()
    password = input("Enter your password: ").strip()

    doctor = next((d for d in m1.doctors if d["email"] == email and d["password"] == password), None)

    if doctor:
        print(f"\nWelcome to {doctor['name']}'s Home Page!")
        doctor_homepage(doctor)
    else:
        print("\nInvalid credentials. Try again.")
        doctor_login()

# Doctor homepage
def doctor_homepage(doctor):
    while True:
        print("\nChoose an option:")
        print("1. View Appointment List")
        print("2. Change Status")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_appointments(doctor)
        elif choice == "2":
            change_doctor_status(doctor)
        elif choice == "3":
            print("\nExiting Doctor Homepage.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# View appointments for a doctor
def view_appointments(doctor):
    doctor_appointments = [a for a in m1.appointments if a["doctor_id"] == doctor["id"]]
    if not doctor_appointments:
        print("\nNo appointments available.")
    else:
        print("\nAppointments:")
        for appointment in doctor_appointments:
            print(f"Patient Name: {appointment['patient_name']}, Disease: {appointment['disease']}")
            print("1. Accept")
            print("2. Reject")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                appointment["status"] = "Accepted"
                print("Appointment Accepted.")
            elif choice == "2":
                appointment["status"] = "Rejected"
                print("Appointment Rejected.")
            else:
                print("Invalid choice. Skipping.")

# Change doctor status
def change_doctor_status(doctor):
    print("\nChange your status:")
    print("1. Waiting")
    print("2. Activated")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        doctor["status"] = "waiting"
    elif choice == "2":
        doctor["status"] = "Activated"
    else:
        print("\nInvalid choice.")
    print(f"\nStatus changed to: {doctor['status']}")