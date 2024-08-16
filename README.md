**_Library Management System_**
================================

**_Overview_**
-----------

The **_Library Management System_** is a comprehensive software solution designed to manage the daily operations of a library. The system allows librarians to efficiently manage books, users, borrowing, and returning of books, and track fines and reservations.

**_Features_**
------------

* **_Book Management_**: Add, remove, and display books in the library
* **_User Management_**: Add, remove, and display users with roles (Admin/Regular)
* **_Borrowing and Returning Books_**: Users can borrow and return books, with fines incurred for overdue books
* **_Reservation System_**: Users can reserve books that are currently borrowed
* **_Fine Management_**: Charge fines for overdue books
* **_Transaction Logs_**: Maintain a log of all transactions (borrowing and returning of books)

**_Classes_**
------------

The system consists of four classes:

### 1. **_Book_** Class

* Represents a book in the library
* Attributes: `title`, `author`, `isbn`, `copies`, `borrowed_copies`, `reserved_copies`
* Methods: `__init__`, `__str__`

### 2. **_User_** Class

* Represents a user of the library
* Attributes: `name`, `role`, `borrowed_books`, `fines`
* Methods: `__init__`, `__str__`

### 3. **_Library_** Class

* Represents the library itself
* Attributes: `books`, `users`
* Methods: `add_book`, `remove_book`, `display_books`, `add_user`, `display_users`, `borrow_book`, `return_book`, `charge_fine`, `reserve_book`, `display_transactions`

### 4. **_Screens_** Class

* Handles user input and output
* Attributes: None
* Methods: `display_menu`, `get_user_input`, `display_books`, `display_users`, `borrow_book`, `return_book`, `charge_fine`, `reserve_book`

**_How to Use_**
--------------

1. Run the program by executing the `main.py` file.
2. Follow the menu prompts to perform various actions, such as adding books, users, borrowing, and returning books, and charging fines.
3. Use the **_Screens_** class to interact with the system.

**_Technical Requirements_**
-------------------------

* Python 3.x
* colorma 0.4.6

**_License_**
---------

This project is licensed under the MIT License. See **_LICENSE_** file for details.

**_Authors_**
---------

[MohammedAhmedHosein]

**_Version_**
---------

1.0.0

**_Date_**
---------

[8/16/2024]
