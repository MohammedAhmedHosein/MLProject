# Library Management System

## Overview

The **Library Management System** is a comprehensive software solution designed to manage the daily operations of a library. The system allows librarians to efficiently manage books, users, borrowing, and returning of books, and track fines and reservations.

## Features

* **Book Management**: Add, remove, and display books in the library.
* **User Management**: Add, remove, and display users with roles (Admin/Regular).
* **Borrowing and Returning Books**: Users can borrow and return books, with fines incurred for overdue books.
* **Reservation System**: Users can reserve books that are currently borrowed.
* **Fine Management**: Charge fines for overdue books.
* **Transaction Logs**: Maintain a log of all transactions (borrowing and returning of books).

## Classes

The system consists of four main classes:

### 1. Book Class

* Represents a book in the library.
* **Attributes**: `title`, `author`, `isbn`, `copies`, `borrowed_copies`, `reserved_copies`, `available_copies`.
* **Methods**: `__init__`, `__str__`.

### 2. User Class

* Represents a user of the library.
* **Attributes**: `name`, `role`, `borrowed_books`, `fines`.
* **Methods**: `__init__`, `__str__`.

### 3. Library Class

* Represents the library itself.
* **Attributes**: `books`, `users`, `transaction_log`.
* **Methods**:
  - `add_book`: Add a new book to the library.
  - `remove_book`: Remove an existing book from the library.
  - `display_books`: Display all books in the library.
  - `add_user`: Add a new user to the library.
  - `display_users`: Display all users in the library.
  - `borrow_book`: Allow a user to borrow a book.
  - `return_book`: Allow a user to return a book and update the availability.
  - `charge_fine`: Charge a fine for overdue books.
  - `reserve_book`: Allow users to reserve books that are currently borrowed.
  - `display_transactions`: Display all transaction logs.
  - `log_transaction`: Log a transaction for borrowing or returning books.

### 4. Screens Class

* Handles user input and output.
* **Attributes**: None.
* **Methods**:
  - `display_menu`: Show the main menu to the user.
  - `get_user_input`: Get input from the user.
  - `display_books`: Display a list of books.
  - `display_users`: Display a list of users.
  - `borrow_book`: Allow the user to borrow a book.
  - `return_book`: Allow the user to return a book.
  - `charge_fine`: Allow the user to pay fines.
  - `reserve_book`: Allow the user to reserve a book.

## Transaction Logging

* **log_transaction**: Records details of all transactions, including who performed the action, what action was performed, which book was involved, and when the transaction occurred. This information is logged in the `transaction_log` attribute of the `Library` class.

* **display_transaction_log**: Displays all recorded transactions in a readable format, showing user actions, book titles, and dates.

## How to Use

1. Run the program by executing the `main.py` file.
2. Follow the menu prompts to perform various actions, such as adding books, users, borrowing, and returning books, and charging fines.
3. Use the **Screens** class to interact with the system.

## Technical Requirements

* Python 3.x
* colorma 0.4.6


## Authors

[MohammedAhmedHosein]

## Version

1.0.0

## Date

8/20/2024
