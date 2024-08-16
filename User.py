class User :

    def __init__(self , name , role):
        self.name = name
        self.role = role
        self.Borrowed_Books=  []
        self.Fines = 0

    def __str__(self):
        return f"{self.name} ({self.role}) - Borrowed Books : {', '.join([book.title for book in self.Borrowed_Books])}, Fines: {self.Fines}"
