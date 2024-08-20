from colorama import Fore, Style

import User
from Library import Library
Library = Library()

def Book_Management():
    while True:
        print(Fore.LIGHTGREEN_EX ,"\n=== Book Management System ===")
        print(Fore.LIGHTCYAN_EX,"1) Add Book")
        print(Fore.LIGHTCYAN_EX,"2) Remove Book")
        print(Fore.LIGHTCYAN_EX,"3) Display Books")
        print(Fore.LIGHTRED_EX,"b) Back",Style.RESET_ALL)
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            title = input("Enter title : ")
            author = input("Enter author : ")
            isb = input("Enter ISB : ")
            copies = input("Enter number of copies : ") #dont forget to make the validaton later
            Library.Add_Book(title,author,isb,copies)
        elif choice == '2':
            isb = input("Enter ISB : ")
            Library.Remove_Book(isb)
        elif choice == '3':
            Library.Display_Books()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'b' to go back.")


def User_Management():
    while True:
        print(Fore.LIGHTGREEN_EX ,"\n=== User Management System ===")
        print(Fore.LIGHTCYAN_EX,"1) Add User")
        print(Fore.LIGHTCYAN_EX,"2) Display User Details")
        print(Fore.LIGHTRED_EX,"b) Back",Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            username = input("Enter your username: ")
            role = input("Enter your role: ")
            Library.Add_User(username, role)
        elif choice == '2':
            Library.Display_Users()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 'b' to go back.")


def Borrow_Return_Books():
    while True:
        print(Fore.LIGHTGREEN_EX  ,"\n=== Borrowing and Returning Books ===")
        print(Fore.LIGHTCYAN_EX,"1) Borrow Book")
        print(Fore.LIGHTCYAN_EX,"2) Return Book")
        print(Fore.LIGHTCYAN_EX,"3) Reserve Book")
        print(Fore.LIGHTRED_EX,"b) Back",Style.RESET_ALL)


        choice = input("Enter your choice: ").strip()

        if choice == '1':

            username = input("Enter User : ")
            isbn = input("Enter isbn : ")
            Library.Borrow_Book(username ,isbn)
        elif choice == '2':
            username = input("Enter User : ")
            isbn = input("Enter isbn : ")
            Library.Return_Book(username,isbn)
            pass
        elif choice == '3':
            user = input("Enter User : ")
            isbn = input("Enter isbn : ")
            Library.Reserve_Book(user, isbn)
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'b' to go back.")


def Fine_Management():
    while True:
        print(Fore.LIGHTGREEN_EX ,"\n=== Fine Management System ===")
        print(Fore.LIGHTCYAN_EX,"1) Calculate Fine")
        print(Fore.LIGHTRED_EX, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            user = input("Enter User : ")
            fine = input("Enter Fine : ")
            Library.Charge_Fine(user,fine)

        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1 or 'b' to go back.")


def Reservation_System():
    while True:
        print(Fore.LIGHTGREEN_EX,"\n=== Reservation System ===")
        print(Fore.LIGHTCYAN_EX,"1) Check Reservations")
        print(Fore.LIGHTRED_EX,"b) Back",Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            user = input("Enter User : ")
            isbn = input("Enter isbn : ")
            Library.Reserved_Book(user,isbn)
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1 or 'b' to go back.")



def main_menu():
    while True:
        print(Fore.LIGHTGREEN_EX,"\n=== Library Management System ===")
        print(Fore.LIGHTCYAN_EX,"1) Book Management")
        print(Fore.LIGHTCYAN_EX,"2) User Management")
        print(Fore.LIGHTCYAN_EX,"3) Borrowing and Returning Books")
        print(Fore.LIGHTCYAN_EX,"4) Fine Management")
        print(Fore.LIGHTCYAN_EX,"5) Reservation System")
        print(Fore.LIGHTRED_EX,"q) Quit",Style.RESET_ALL)

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
        elif choice.lower() == 'q':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5 or 'q' to quit.")
