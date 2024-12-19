
import module1 as m1
def patient_section():
    print("\n1. New Registration")
    print("2. Login")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        new_registration()
    elif choice == "2":
        patient_login()
    else:
        print("\nInvalid choice. Please try again.")
        patient_section()

# New patient registration
def new_registration():
    print("\nNew Registration:")
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    mobile = input("Enter your mobile: ").strip()
    password = input("Enter your password: ").strip()

    m1.patients.append({
        "name": name,
        "age": age,
        "mobile": mobile,
        "password": password
    })
    print("\nRegistration successful!")

# Patient login
def patient_login():
    print("\nPatient Login:")
    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()

    patient = next((p for p in m1.patients if p["name"] == name and p["password"] == password), None)

    if patient:
        print(f"\nWelcome to {patient['name']}'s Home Page!")
        patient_homepage(patient)
    else:
        print("\nInvalid credentials. Try again.")
        patient_login()

# Patient homepage
def patient_homepage(patient):
    while True:
        print("\nChoose an option:")
        print("1. Book Appointment")
        print("2. View Report Status")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_appointment(patient)
        elif choice == "2":
            view_report_status()
        elif choice == "3":
            print("\nExiting Patient Homepage.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Book appointment
def book_appointment(patient):
    print("\nEnter Appointment Details:")
    doctor_id = int(input("Enter doctor ID: ").strip())
    disease = input("Enter disease: ").strip()

    m1.appointments.append({
        "patient_name": patient["name"],
        "doctor_id": doctor_id,
        "disease": disease,
        "status": "Pending"
    })
    print("\nAppointment successfully sent to the doctor.")

# View report status
def view_report_status():
    print("\nReport Status:")
    for appointment in m1.appointments:
        print(f"Patient: {appointment['patient_name']}, Status: {appointment['status']}")
