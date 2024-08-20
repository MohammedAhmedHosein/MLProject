class Book :
    #isbn = International Standard Book Number
    def __init__(self , title , author , isbn , copies):
        self.title  = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.Borrowed_copies = 0
        self.Reserved_copies = 0
        self.available_copies = copies
    def __str__(self):
        return f"{self.title} by {self.author} ISBN[{self.isbn}] - {self.copies} copies -  {self.available_copies} available copies "


