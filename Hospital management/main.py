import module1 as m1
import module2 as m2
import module3 as m3
import module4 as m4
def main_menu():
    while True:
        print("\nWelcome to CCNA Hospital!")
        print("Please choose an option:")
        print("1. Hospital Management")
        print("2. Doctor Login")
        print("3. Staff Login")
        print("4. Patient")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            m1.hospital_management_login()
        elif choice == "2":
            m2.doctor_login()
        elif choice == "3":
            m3.staff_login()
        elif choice == "4":
            m4.patient_section()
        elif choice == "5":
            print("\nExiting the application. Thank you!")
            break
        else:
            print("\nInvalid choice. Please try again.")
main_menu()