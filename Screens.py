from colorama import Fore, Style


def Book_Management():
    while True:
        print(Fore.LIGHTBLUE_EX ,"\n=== Book Management System ===")
        print(Fore.GREEN ,"1) Add Book")
        print(Fore.GREEN ,"2) Remove Book")
        print(Fore.GREEN ,"3) Display Books")
        print(Fore.RED,"b) Back",Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            pass
            #add_book()
        elif choice == '2':
            pass
           #remove_book()
        elif choice == '3':
            pass
           # display_books()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'b' to go back.")


def User_Management():
    while True:
        print(Fore.LIGHTBLUE_EX ,"\n=== User Management System ===")
        print(Fore.GREEN,"1) Add User")
        print(Fore.GREEN,"2) Display User Details")
        print(Fore.RED,"b) Back",Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            pass
            #add_user()
        elif choice == '2':
            pass
            #display_user_details()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 'b' to go back.")


def Borrow_Return_Books():
    while True:
        print(Fore.LIGHTBLUE_EX  ,"\n=== Borrowing and Returning Books ===")
        print(Fore.GREEN,"1) Borrow Book")
        print(Fore.GREEN,"2) Return Book")
        print(Fore.GREEN,"3) Reserve Book")
        print(Fore.RED,"b) Back",Style.RESET_ALL)


        choice = input("Enter your choice: ").strip()

        if choice == '1':
            pass
            #borrow_book()
        elif choice == '2':
            pass
            #return_book()
        elif choice == '3':
            pass
            #reserve_book()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'b' to go back.")


def Fine_Management():
    while True:
        print(Fore.LIGHTBLUE_EX ,"\n=== Fine Management System ===")
        print(Fore.GREEN,"1) Calculate Fine")
        print(Fore.RED, "b) Back", Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            pass
            #calculate_fine()
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please enter 1 or 'b' to go back.")


def Reservation_System():
    while True:
        print(Fore.LIGHTBLUE_EX,"\n=== Reservation System ===")
        print(Fore.GREEN,"1) Check Reservations")
        print(Fore.RED,"b) Back",Style.RESET_ALL)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            pass
            #check_reservations()
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
        print(Fore.RED,"q) Quit",Style.RESET_ALL)

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
