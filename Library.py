from Book import Book
from User import User
from datetime import datetime

class Library:
    def __init__(self):
        self.Books = []
        self.Users = []
        self.Transaction_Log = []

    def Log_Transaction(self, user, action, book):

        transaction = {
            'user': user,
            'action': action,
            'book': book,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.Transaction_Log.append(transaction)
        print(f"Transaction logged: {transaction}")

    def Display_Transaction_Log(self):
        print("Transaction Log:")
        for entry in self.Transaction_Log:

            print(f"User: {entry['user']} | Action: {entry['action']} | Book: {entry['book']} | Date: {entry['date']}")

    def Add_Book(self, author, title, isbn, copies):
        self.Books.append(Book(author, title, isbn, copies))

    def Remove_Book(self, isbn):
        for book in self.Books:
            if book.isbn == isbn:
                self.Books.remove(book)
                return
        print("Book Not Found !!!")

    def Display_Books(self):
        for book in self.Books:
            print(book)

    def Add_User(self, username, role):
        self.Users.append(User(username, role))

    def Display_Users(self):
        for user in self.Users:
            print(user)

    def Borrow_Book(self, username, isbn):
        user = next((u for u in self.Users if u.name == username), None)
        if not user:
            print(f"User {username} not found!")
            return

        book_to_borrow = next((book for book in self.Books if book.isbn == isbn), None)
        if not book_to_borrow:
            print("Book not found!")
            return

        if int(book_to_borrow.copies) > int(book_to_borrow.Borrowed_copies):
            book_to_borrow.Borrowed_copies = str(int(book_to_borrow.Borrowed_copies) + 1)
            user.Borrowed_Books.append(book_to_borrow)
            book_to_borrow.available_copies = str(int(book_to_borrow.available_copies) - 1)
            print(f"{user.name} has borrowed {book_to_borrow.title}")
            self.Log_Transaction(user=user.name, action="borrowed", book=book_to_borrow.title)

        elif int(book_to_borrow.Reserved_copies) > 0:
            print(f"{book_to_borrow.title} is reserved, take another book.")
        else:
            print(f"{book_to_borrow.title} is not available.")
    def Charge_Fine(self, username, overdue):
        user = next((u for u in self.Users if u.name == username), None)
        if not user:
            print(f"User {username} not found!")
            return

        try:
            overdue_amount = float(overdue)
            user.Fines = str(float(user.Fines) + overdue_amount)
            print(f"{user.name} has been charged {overdue_amount} units of fine")
        except ValueError:
            print(f"Invalid fine amount: {overdue}")

    def Return_Book(self, username, isbn, overdue_days=0):
        user = next((u for u in self.Users if u.name == username), None)
        if not user:
            print(f"User {username} not found!")
            return

        book_to_return = next((book for book in self.Books if book.isbn == isbn), None)
        if not book_to_return:
            print(f"Book with ISBN {isbn} not found!")
            return

        if book_to_return not in user.Borrowed_Books:
            print(f"Book {book_to_return.title} is not in {user.name}'s borrowed books.")
            return

        book_to_return.Borrowed_copies = str(int(book_to_return.Borrowed_copies) - 1)
        book_to_return.available_copies = str(int(book_to_return.available_copies) + 1)
        user.Borrowed_Books.remove(book_to_return)
        print(f"{user.name} has returned {book_to_return.title}")

        self.Log_Transaction(user=user.name, action="returned", book=book_to_return.title)


        if overdue_days > 0:
            fine = overdue_days * 1
            self.Charge_Fine(username, fine)

        if int(book_to_return.Borrowed_copies) < int(book_to_return.copies) and int(book_to_return.Reserved_copies) > 0:
            book_to_return.Reserved_copies = str(int(book_to_return.Reserved_copies) - 1)
            print(f"There were reservations for {book_to_return.title}. Now available.")



    def Reserve_Book(self, username, isbn):
        user = next((u for u in self.Users if u.name == username), None)
        if not user:
            print(f"User {username} not found!")
            return

        book_to_reserve = next((book for book in self.Books if book.isbn == isbn), None)
        if not book_to_reserve:
            print("Book not found!")
            return

        if int(book_to_reserve.copies) > int(book_to_reserve.Borrowed_copies):
            print(f"{book_to_reserve.title} is available for borrowing, no need to reserve.")
            return

        if book_to_reserve in user.Reserved_Books:
            print(f"{user.name} has already reserved {book_to_reserve.title}.")
            return

        book_to_reserve.Reserved_copies = str(int(book_to_reserve.Reserved_copies) + 1)
        user.Reserved_Books.append(book_to_reserve)
        print(f"{user.name} has successfully reserved {book_to_reserve.title}")

    def Reserved_Book(self, username, isbn):

        user = None
        for u in User.Users:
            if u.name == username:
                user = u
                break

        if not user:
            print(f"User {username} not found!")
            return


        book_to_reserve = None
        for book in self.Books:
            if book.isbn == isbn:
                book_to_reserve = book
                break

        if not book_to_reserve:
            print(f"Book with ISBN {isbn} not found!")
            return

        if int(book_to_reserve.copies) > int(book_to_reserve.Borrowed_copies):
            print(f"{book_to_reserve.title} is available for borrowing, no need to reserve.")
            return


        if book_to_reserve in user.Reserved_Books:
            print(f"{user.name} has already reserved {book_to_reserve.title}.")
            return


        book_to_reserve.Reserved_copies = str(int(book_to_reserve.Reserved_copies) + 1)
        user.Reserved_Books.append(book_to_reserve)
        print(f"{user.name} has successfully reserved {book_to_reserve.title}.")

        return


