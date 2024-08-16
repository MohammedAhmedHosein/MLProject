from Book import Book
from User import User


class Library :
    def __init__(self):
        self.Books = []
        self.Users = []

    def Add_Book(self, author , title , isbn , copies):
        self.Books.append(Book(author , title , isbn , copies))

    def Remove_Book(self , isbn):
        for book in self.Books:
            if book.isbn == isbn:
                self.Books.remove(book)
                return
        print("Book Not Found !!!")

    def Display_Books(self):
        for book in self.Books:
            print(book)

    def Add_User(self ,username , role):
        self.Users.append(User(username , role))

    def Display_Users(self):
        for user in self.Users:
            print(user)


    def Borrow_Book(self , user , isbn):
        for book in self.Books:
            if book.isbn == isbn:
                if book.copies > book.Borrowed_copies :
                    book.Borrowed_copies +=1
                    user.Borrowed_Books.append(book)
                    print(f"{user.name} has borrowed {book.title} ")
                    return
                elif book.Reserved_copies > 0:
                    print(f"{book.title} is Reserved , Take Another Book ")
                    return
                else:
                    print(f"{book.title} is not Available ")
                    return
        print("Book Not Found !!!")


