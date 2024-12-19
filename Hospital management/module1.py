
hospital_username = "admin"
hospital_password = "password"

doctors = []
staff = []
patients = []
appointments = []






def add_doctor():
    while True:
        try:
            print("\nAdding Doctor Details:")
            doctor_id = len(doctors) + 1
            name = input("Enter doctor name: ").strip()
            email = input("Enter email ID: ").strip()
            password = input("Enter password: ").strip()
            specialization = input("Enter specialization: ").strip()
            experience = int(input("Enter experience (in years): "))
            status = input("Enter status (waiting/activated): ").strip()
            if not all([name, email, password, specialization, experience]):
                print("\nOne or more fields are empty. Please try again.")
            else:
                doctors.append({
                "id": doctor_id,
                "name": name,
                "email": email,
                "password": password,
                "specialization": specialization,
                "experience": experience,
                "status": status
                })
                print("\nDoctor details successfully added.")
                break

        except(ValueError,UnboundLocalError):
            print("Enter Valid details only...")
            add_doctor()

        
       

def add_staff():
    while True:
        try:
            print("\nAdding Staff Member Details:")
            staff_id = len(staff) + 1
            name = input("Enter staff name: ").strip()
            email = input("Enter email ID: ").strip()
            password = input("Enter password: ").strip()
            specialization = input("Enter specialization: ").strip()
            experience = int(input("Enter experience (in years): "))
            if not all([name, email, password, specialization, experience]):
                print("\nOne or more fields are empty. Please try again.")
            else:
                staff.append({
                "id": staff_id,
                "name": name,
                "email": email,
                "password": password,
                "specialization": specialization,
                "experience": experience
                })
                print("\nStaff member details successfully added.")
                break
        except(ValueError,UnboundLocalError):
            print("Enter Valid details only...")
            add_staff()

        
        

# Display doctor details
def display_doctor_details():
    if not doctors:
        print("\nNo doctor details available.")
    else:
        print("\nDoctor Details:")
        for doctor in doctors:
            print(f"ID: {doctor['id']}, Name: {doctor['name']}, Specialization: {doctor['specialization']}, Status: {doctor['status']}, experience:{doctor['experience']}")

# Display staff details
def display_staff_details():
    if not staff:
        print("\nNo staff details available.")
    else:
        print("\nStaff Details:")
        for member in staff:
            print(f"ID: {member['id']}, Name: {member['name']}, Specialization: {member['specialization']}, experience:{member['experience']}")


def staff_login():
    print("\nWelcome to Staff Login Page.")
    email = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    staff_member = next((s for s in staff if s["email"] == email and s["password"] == password), None)

    if staff_member:
        print(f"\nWelcome to {staff_member['name']}'s Home Page!")
        staff_homepage()
    else:
        print("\nInvalid credentials. Try again.")
        staff_login()


def staff_homepage():
    while True:
        print("\nChoose an option:")
        print("1. Patient Appointments List")
        print("2. Doctor List")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            patient_appointment()
        elif choice == "2":
            display_doctor_details()
        elif choice == "3":
            print("\nExiting Staff Homepage.")
            break
        else:
            print("\nInvalid choice. Please try again.")


def patient_appointment():
    print("\nEnter Appointment Details:")
    patient_name = input("Enter patient name: ").strip()
    doctor_id = int(input("Enter doctor ID: ").strip())
    disease = input("Enter disease: ").strip()

    appointments.append({
        "patient_name": patient_name,
        "doctor_id": doctor_id,
        "disease": disease,
        "status": "Pending"
    })
    print("\nAppointment successfully sent to the doctor.")

def hospital_management_homepage():
    while True:
        print("\nChoose an option:")
        print("1. Doctor Details")
        print("2. Staff Details")
        print("3. Add Doctor")
        print("4. Add Staff Members")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_doctor_details()
        elif choice == "2":
            display_staff_details()
        elif choice == "3":
            add_doctor()
        elif choice == "4":
            add_staff()
        elif choice == "5":
            print("\nExiting Hospital Management.")
            break
        else:
            print("\nInvalid choice. Please try again.")

def hospital_management_login():
    print("\nWelcome to the Hospital Management Login Page.")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username == hospital_username and password == hospital_password:
        print("\nLogin Successful! Welcome to Hospital Management Home Page.")
        hospital_management_homepage()
    else:
        print("\nInvalid credentials. Try again.")
        hospital_management_login()





    