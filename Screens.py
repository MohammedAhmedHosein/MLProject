from colorama import Fore, Style
from Library import Library

library = Library()


def Book_Management():
    while True:
        print(Fore.LIGHTGREEN_EX, "\n=== Book Management System ===")
        print(Fore.LIGHTCYAN_EX, "1) Add Book")
        print(Fore.LIGHTCYAN_EX, "2) Remove Book")
        print(Fore.LIGHTCYAN_EX, "3) Display Books")
        print(Fore.LIGHTRED_EX, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            copies = input("Enter number of copies: ")
            library.Add_Book(title, author, isbn, copies)
        elif choice == '2':
            isbn = input("Enter ISBN: ")
            library.Remove_Book(isbn)
        elif choice == '3':
            library.Display_Books()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'b' to go back.")


def User_Management():
    while True:
        print(Fore.LIGHTGREEN_EX, "\n=== User Management System ===")
        print(Fore.LIGHTCYAN_EX, "1) Add User")
        print(Fore.LIGHTCYAN_EX, "2) Display User Details")
        print(Fore.LIGHTRED_EX, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            username = input("Enter username: ")
            role = input("Enter role: ")
            library.Add_User(username, role)
        elif choice == '2':
            library.Display_Users()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 'b' to go back.")


def Borrow_Return_Books():
    while True:
        print(Fore.LIGHTGREEN_EX, "\n=== Borrowing and Returning Books ===")
        print(Fore.LIGHTCYAN_EX, "1) Borrow Book")
        print(Fore.LIGHTCYAN_EX, "2) Return Book")
        print(Fore.LIGHTCYAN_EX, "3) Reserve Book")
        print(Fore.LIGHTRED_EX, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            username = input("Enter username: ")
            isbn = input("Enter ISBN: ")
            library.Borrow_Book(username, isbn)
        elif choice == '2':
            username = input("Enter username: ")
            isbn = input("Enter ISBN: ")
            overdue_days = int(input("Enter overdue days (if any, else 0): "))
            library.Return_Book(username, isbn, overdue_days)
        elif choice == '3':
            username = input("Enter username: ")
            isbn = input("Enter ISBN: ")
            library.Reserve_Book(username, isbn)
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'b' to go back.")


def Fine_Management():
    while True:
        print(Fore.LIGHTGREEN_EX, "\n=== Fine Management System ===")
        print(Fore.LIGHTCYAN_EX, "1) Charge Fine")
        print(Fore.LIGHTRED_EX, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            username = input("Enter username: ")
            fine = float(input("Enter fine amount: "))
            library.Charge_Fine(username, fine)
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1 or 'b' to go back.")


def Reservation_System():
    while True:
        print(Fore.LIGHTGREEN_EX, "\n=== Reservation System ===")
        print(Fore.LIGHTCYAN_EX, "1) Check Reservations")
        print(Fore.LIGHTRED_EX, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            username = input("Enter username: ")
            isbn = input("Enter ISBN: ")
            library.Reserved_Book(username, isbn)
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1 or 'b' to go back.")

def Transaction_logs():
    Library.Display_Transaction_Log(library)
def main_menu():
    while True:
        print(Fore.LIGHTGREEN_EX, "\n=== Library Management System ===")
        print(Fore.LIGHTCYAN_EX, "1) Book Management")
        print(Fore.LIGHTCYAN_EX, "2) User Management")
        print(Fore.LIGHTCYAN_EX, "3) Borrowing and Returning and Reserve Books")
        print(Fore.LIGHTCYAN_EX, "4) Fine Management")
        print(Fore.LIGHTCYAN_EX, "5) Reservation System")
        print(Fore.LIGHTCYAN_EX, "6) Transaction Log System")
        print(Fore.LIGHTRED_EX, "q) Quit", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            Book_Management()
        elif choice == '2':
            User_Management()
        elif choice == '3':
            Borrow_Return_Books()
        elif choice == '4':
            Fine_Management()
        elif choice == '5':
            Reservation_System()
        elif choice == '6':
            Transaction_logs()
        elif choice.lower() == 'q':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5 or 'q' to quit.")