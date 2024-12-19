import module2 as m2
import module4 as m4
def staff_login():
    print("\nWelcome to Staff Login Page.")
    email = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    staff_member = next((s for s in m2.staff if s["email"] == email and s["password"] == password), None)

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
           m4.patient_appointment()
        elif choice == "2":
           m2.display_doctor_details()
        elif choice == "3":
            print("\nExiting Staff Homepage.")
            break
        else:
            print("\nInvalid choice. Please try again.")
