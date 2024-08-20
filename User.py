class User:
    Users = []

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.Borrowed_Books = []
        self.Reserved_Books = []
        self.Fines = 0
        User.Users.append(self)

    def __str__(self):
        borrowed_books = ', '.join(f"[{book.title}]" for book in self.Borrowed_Books) or "[None]"
        reserved_books = ', '.join(f"[{book.title}]" for book in self.Reserved_Books) or "[None]"
        return (
            f"User: {self.name} | "
            f"Role: {self.role} | "
            f"Borrowed Books: {borrowed_books} | "
            f"Reserved Books: {reserved_books} | "
            f"Fines: {self.Fines} units"

        )
