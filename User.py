class User :

    def __init__(self , name , role):
        self.name = name
        self.role = role
        self.Borrowed_Books=  []
        self.Fines = 0

    def __str__(self):
        borrowed_books = ', '.join(book.title for book in self.Borrowed_Books) or "None"
        return (
            f"User: {self.name} - "
            f"Role: {self.role} - "
            f"Borrowed Books: {borrowed_books} - "
            f"Fines: {self.Fines}"
        )

